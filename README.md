# Browserbase MCP Server

A Type 3 DAuth MCP server for [Browserbase](https://browserbase.com) API. Provides cloud browser automation capabilities for AI agents.

## Features

- **Create Session** — Launch a cloud browser instance
- **Get Session** — Retrieve session details and debugging URL
- **List Sessions** — View all active and recent sessions
- **Get Recording** — Access session recordings
- **Get Logs** — Retrieve browser console logs
- **End Session** — Terminate a browser session

## Authentication

This server uses **Type 3 DAuth** (Dedalus Auth) — your API key is encrypted client-side and decrypted in a secure Dedalus enclave.

### Get Your Browserbase API Key

1. Go to https://browserbase.com
2. Sign up and get an API key
3. Copy the key

## Installation

```bash
git clone https://github.com/dedalus-labs/browserbase-mcp.git
cd browserbase-mcp
pip install -e .
cp .env.example .env
# Edit .env and add BROWSERBASE_API_KEY
```

## Available Tools

### `browserbase_create_session`

Create a new browser automation session.

```python
browserbase_create_session(
    project_id="optional-project-id",
    headless=True,
    browser="chrome",
)
```

### `browserbase_get_session`

Get details of a browser session.

```python
browserbase_get_session(
    session_id="session-id-here",
)
```

### `browserbase_list_sessions`

List all browser sessions.

```python
browserbase_list_sessions(
    limit=20,
    offset=0,
)
```

### `browserbase_get_session_recording`

Get the recording of a browser session.

```python
browserbase_get_session_recording(
    session_id="session-id-here",
)
```

### `browserbase_get_session_logs`

Get logs from a browser session.

```python
browserbase_get_session_logs(
    session_id="session-id-here",
)
```

### `browserbase_end_session`

End a browser session.

```python
browserbase_end_session(
    session_id="session-id-here",
)
```

## Pricing

Browserbase offers pay-per-use pricing. Check https://browserbase.com/pricing for details.

## Deploy to Dedalus

1. Push to GitHub (public repo)
2. Go to https://www.dedaluslabs.ai/dashboard
3. Add Server → Connect GitHub repo
4. Set `BROWSERBASE_API_KEY` as Required Credential
5. Deploy

## License

MIT