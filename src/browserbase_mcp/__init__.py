# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Browserbase AI MCP server for Dedalus.

Provides cloud browser automation capabilities via Browserbase.
Credentials provided by clients at runtime via DAuth token exchange.
"""

from __future__ import annotations

from browserbase_mcp.config import create_browserbase_connection
from browserbase_mcp.tools import browserbase_tools

__all__ = ["create_browserbase_connection", "browserbase_tools"]