# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Tool registry for browserbase-mcp.

Modules:
  sessions  -- browserbase_create_session, browserbase_get_session,
               browserbase_list_sessions, browserbase_get_session_recording,
               browserbase_get_session_logs, browserbase_end_session
"""

from __future__ import annotations

from browserbase_mcp.tools.sessions import session_tools

browserbase_tools = [
    *session_tools,
]