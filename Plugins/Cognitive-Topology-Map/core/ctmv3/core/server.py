"""
CTMv3 Persistent Server
========================
Provenance: CTMv3 Engine v1.3.0 — 2026-06-12
Purpose: HTTP server exposing workspace state for agent consumption.
         No external dependencies — stdlib http.server only.

Architecture:
  CTMv3Server      — owns the registry and HTTP server, starts/stops them
  _RequestHandler  — routes GET/POST requests against the registry
  DEFAULT_PORT     — 7430 (memorable, unlikely collision)

Endpoints:
  GET  /health                          liveness probe
  GET  /projects                        list all watched projects
  POST /projects/register               register a new project path {"path": "..."}
  GET  /projects/<name>                 full project state
  GET  /projects/<name>/context         compact agent context blob (primary endpoint)
  POST /projects/<name>/refresh         force immediate state refresh

The /context endpoint is the primary interface for agents entering a project.
Instead of running `ctmv3 chain`, an agent calls:
  GET /projects/<name>/context
and receives exactly the state it needs — branch, tasks, fingerprint, suggestion.
"""

from __future__ import annotations

import json
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from ctmv3.core.watcher import ProjectRegistry

logger = logging.getLogger(__name__)

DEFAULT_PORT: int = 7430


def _json_response(handler: BaseHTTPRequestHandler, data: dict, status: int = 200) -> None:
    body = json.dumps(data, indent=2, default=str).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _error(handler: BaseHTTPRequestHandler, msg: str, status: int = 400) -> None:
    _json_response(handler, {"error": msg}, status)


class _RequestHandler(BaseHTTPRequestHandler):

    def log_message(self, fmt: str, *args) -> None:  # type: ignore[override]
        logger.debug("http: " + fmt, *args)

    @property
    def _registry(self) -> ProjectRegistry:
        return self.server.registry  # type: ignore[attr-defined]

    def _route_get(self, path: str) -> None:
        if path == "/health":
            from ctmv3.core import __version__
            _json_response(self, {
                "status": "ok",
                "server": "ctmv3",
                "version": __version__,
                "projects": len(self._registry.list_all()),
            })
            return

        if path == "/projects":
            projects = self._registry.list_all()
            _json_response(self, {
                "count": len(projects),
                "projects": [
                    {
                        "name": p.name,
                        "path": str(p.path),
                        "branch": p.inventory.branch if p.inventory else "UNKNOWN",
                        "last_refreshed": p.last_refreshed.isoformat() if p.last_refreshed else None,
                    }
                    for p in projects
                ],
            })
            return

        parts = [x for x in path.split("/") if x]
        if len(parts) >= 2 and parts[0] == "projects":
            name_or_key = parts[1]
            ps = self._registry.get_by_name(name_or_key)
            if ps is None:
                _error(self, f"project not found: {name_or_key!r}", 404)
                return

            if len(parts) == 3 and parts[2] == "context":
                _json_response(self, ps.to_context())
            else:
                ctx = ps.to_context()
                ctx["inventory"] = ps.inventory.to_dict() if ps.inventory else {}
                ctx["session_state_raw"] = ps.session_state
                _json_response(self, ctx)
            return

        _error(self, f"not found: {path}", 404)

    def _route_post(self, path: str, body: bytes) -> None:
        if path == "/projects/register":
            try:
                data = json.loads(body) if body else {}
            except json.JSONDecodeError:
                _error(self, "invalid JSON body")
                return
            project_path = data.get("path", "")
            if not project_path:
                _error(self, "missing 'path' in request body")
                return
            p = Path(project_path).resolve()
            if not p.exists():
                _error(self, f"path does not exist: {p}", 422)
                return
            ps = self._registry.register(p)
            _json_response(self, ps.to_context(), 201)
            return

        parts = [x for x in path.split("/") if x]
        if len(parts) == 3 and parts[0] == "projects" and parts[2] == "refresh":
            ps = self._registry.get_by_name(parts[1])
            if ps is None:
                _error(self, f"project not found: {parts[1]!r}", 404)
                return
            ps.refresh()
            _json_response(self, ps.to_context())
            return

        _error(self, f"not found: {path}", 404)

    def do_GET(self) -> None:
        self._route_get(urlparse(self.path).path)

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length > 0 else b""
        self._route_post(path, body)


class CTMv3Server:
    """
    Persistent CTMv3 workspace state server.

    Owns a ProjectRegistry (background poll watcher) and an HTTPServer.
    Agents query /projects/<name>/context instead of running ctmv3 chain.
    """

    def __init__(self, port: int = DEFAULT_PORT, poll_interval: float = 5.0) -> None:
        self.port = port
        self.registry = ProjectRegistry(poll_interval=poll_interval)
        self._http: Optional[HTTPServer] = None

    def register_project(self, path: Path) -> None:
        self.registry.register(Path(path).resolve())

    def scan_and_register(self, root: Path, max_depth: int = 3) -> int:
        """Auto-discover CTM-activated projects under root and register them."""
        from ctmv3.core.boot import discover, discover_all
        count = 0
        try:
            inventories = discover_all(root, max_depth=max_depth)
            for inv in inventories:
                self.registry.register(inv.project_root)
                count += 1
        except Exception as exc:
            logger.warning("scan_and_register: discover_all failed: %s", exc)

        # Also register root itself if it has tier1 signals
        try:
            root_inv = discover(root)
            if root_inv.tier1_signals:
                self.registry.register(root)
                count += 1
        except Exception:
            pass

        return count

    def start(self, block: bool = True) -> None:
        """Start the watcher and HTTP server. block=True runs until Ctrl-C."""
        self.registry.start_polling()

        self._http = HTTPServer(("127.0.0.1", self.port), _RequestHandler)
        self._http.registry = self.registry  # type: ignore[attr-defined]

        url = f"http://127.0.0.1:{self.port}"
        logger.info("CTMv3 server listening on %s", url)
        print(f"CTMv3 server listening on {url}", flush=True)
        print(f"  /health          — liveness probe", flush=True)
        print(f"  /projects        — list watched projects", flush=True)
        print(f"  /projects/<name>/context — agent context blob", flush=True)

        if block:
            try:
                self._http.serve_forever()
            except KeyboardInterrupt:
                pass
            finally:
                self.stop()
        else:
            t = threading.Thread(
                target=self._http.serve_forever,
                daemon=True,
                name="ctmv3-http",
            )
            t.start()

    def stop(self) -> None:
        self.registry.stop_polling()
        if self._http:
            self._http.shutdown()
            self._http = None
        logger.info("CTMv3 server stopped")
