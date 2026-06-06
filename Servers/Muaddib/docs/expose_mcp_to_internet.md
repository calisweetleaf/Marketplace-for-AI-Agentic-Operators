# Exposing Sovereign MCP to ChatGPT, Grok, and Remote Clients

This guide explains how to expose your locally running `https_wrapper.py` to the public internet using secure tunnels. This enables external platforms like **ChatGPT (Custom Actions)**, **Grok**, and **remote agents** to access your MCP server.

---

## 1. The Core Prerequisite: The `--external` Flag

By default, `https_wrapper.py` only accepts connections from `localhost`.

* Tunnels like `ngrok` or Cloudflare forward external requests and append headers such as `X-Forwarded-For`.
* If you do not run the server in external mode, the security controller will block these requests.

### Start Command

To run the server and allow proxy/tunnel connections, launch it with the `--external` flag:

```bash
# In your project directory inside the .venv
python https_wrapper.py --external --host 0.0.0.0 --port 8443
```

---

## 2. Exposing the Server via a Public Tunnel

Since external services require a publicly trusted SSL certificate (self-signed certificates will be rejected by OpenAI/Grok), you must use a tunnel service. The tunnel agent terminates SSL at their edge with a trusted certificate and forwards the traffic locally.

Here are the two best options:

### Option A: Ngrok (Fastest Setup)

1. **Install Ngrok**:
   Ensure you have `ngrok` installed. If not, install it via your package manager:

   ```bash
   sudo snap install ngrok  # Or download from ngrok.com
   ```

2. **Start the Tunnel**:
   Because `https_wrapper.py` serves HTTPS using a self-signed certificate, you must tell ngrok to ignore local certificate validation errors:

   ```bash
   ngrok http https://localhost:8443 --insecure-skip-verify
   ```

3. **Copy the Public URL**:
   Ngrok will output a URL like:
   `https://your-subdomain.ngrok-free.app`

---

### Option B: Cloudflare Tunnels (Free & Highly Configurable)

Cloudflare Tunnels are completely free, support custom domains, and do not show ngrok's warning page.

1. **Install Cloudflare's tunnel daemon (`cloudflared`)**:

   ```bash
   sudo apt-get install cloudflared  # On Debian/Ubuntu
   ```

2. **Run a Quick Tunnel**:
   Start a quick tunnel bypassing SSL validation:

   ```bash
   cloudflared tunnel --url https://localhost:8443 --no-tls-verify
   ```

3. **Copy the Public URL**:
   Cloudflare will print a random subdomain like:
   `https://some-random-words.trycloudflare.com`

---

## 3. Configuring ChatGPT Custom Actions

Once your tunnel is running and you have your public URL, you can register it as an Action in ChatGPT:

1. **Go to GPT Editor**:
   * Open ChatGPT -> **Explore GPTs** -> **Create a GPT**.
   * Go to the **Configure** tab and scroll down to click **Create new action**.

2. **Import the OpenAPI Spec**:
   * Our server dynamically generates the exact OpenAPI 3.1 specification at `/openapi.json`.
   * Click **Import from URL** in ChatGPT and enter:
     `https://<your-tunnel-domain>/openapi.json?api_key=<YOUR_API_KEY>`
   * Or retrieve the spec content locally and paste it into the schema editor.

3. **Configure Authentication**:
   * Set **Authentication Type** to **API Key**.
   * Choose **Bearer** as the format.
   * Paste your secret API key (found in `data/security/api_key.txt`).

4. **Test an Endpoint**:
   * Try calling a low-risk endpoint like `/health` or listing the tools. ChatGPT will guide you through approving the connection.

---

## 4. Configuring Grok or Custom LLM Integrations

For systems like Grok, remote Python scripts, or custom webhooks:

### Direct API Calls (REST)

External scripts can query the wrapper directly by passing the key in the header:

```http
GET https://<your-tunnel-domain>/tools
Authorization: Bearer <YOUR_API_KEY>
```

### Receiving Event Streams (SSE / Webhooks)

* For real-time telemetry, remote clients can establish an EventSource connection to `https://<your-tunnel-domain>/events?api_key=<YOUR_API_KEY>`.
* Webhooks can be registered by POSTing to `/webhooks/register`:

  ```bash
  curl -X POST https://<your-tunnel-domain>/webhooks/register \
    -H "Authorization: Bearer <YOUR_API_KEY>" \
    -H "Content-Type: application/json" \
    -d '{"callback_url": "https://your-receiver.com/webhook", "secret": "your_signing_secret"}'
  ```

---

## 5. Security Checklist

* [ ] **API Key**: Keep the key in `data/security/api_key.txt` confidential. It acts as the password to your local system.
* [ ] **Tunnels**: Terminate/stop the tunnel process (`Ctrl+C`) when you are done to shut down public access immediately.
* [ ] **Rate Limiting**: The server enforces a rate limit of 100 requests per minute by default. You can adjust this configuration inside `https_wrapper.py` or `config_manager.py` if your LLM runs into limits during parallel operations.
