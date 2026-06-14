# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Browserbase API configuration."""

from dedalus_mcp.auth import Connection, SecretKeys

# Browserbase API base URL
BROWSERBASE_API_BASE = "https://api.browserbase.com/v1"


def create_browserbase_connection() -> Connection:
    """Create a DAuth connection to Browserbase API.

    Uses Bearer token authentication.
    The API key is encrypted client-side and decrypted in the Dedalus enclave.

    Returns:
        Configured Connection for Browserbase API.

    """
    return Connection(
        name="browserbase",
        secrets=SecretKeys(token="BROWSERBASE_API_KEY"),
        base_url=BROWSERBASE_API_BASE,
        auth_header_format="Bearer {api_key}",
    )