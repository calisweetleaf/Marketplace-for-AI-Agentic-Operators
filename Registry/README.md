# Registry

This directory contains public release metadata for the Aeriadne / Somnus Intelligence Stack.

The active public plugin surface is the triad:

- `Aeriadne`
- `Cognitive-Topology-Map` / `CTMv3`
- `Mentat`

`plugins.yaml` separates package payload versions from release posture:

- `package_version` is the installable package or manifest version.
- `release_status` is the public release posture.
- `source` is the public release path inside this repository.
- `version_evidence` points to public files that justify the version claim.

Muadib / Sovereign BB7 is not a plugin package. It is a curated server-plane release surface under `Servers/Muaddib/`.

This registry is not a broad mirror of the private lab. Extra lab support surfaces, runtime state, cache state, local Codex plugin cache paths, and raw server trees are intentionally excluded from the public plugin registry.
