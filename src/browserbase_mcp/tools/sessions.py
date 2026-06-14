# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Session management tools for Browserbase."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from browserbase_mcp.guards import (
    validate_browser,
    validate_limit,
    validate_offset,
    validate_project_id,
    validate_session_id,
)
from browserbase_mcp.request import _bool, _int, _opt_str, request
from browserbase_mcp.types import JSONObject


@tool(
    description="Create a new browser automation session.",
    tags=["sessions", "write"],
    annotations=ToolAnnotations(readOnlyHint=False),
)
async def browserbase_create_session(
    project_id: str | None = None,
    headless: bool = True,
    browser: str = "chrome",
) -> JSONObject:
    """Create a new browser session.

    Args:
        project_id: Optional project ID.
        headless: Run browser in headless mode.
        browser: Browser type (chrome, firefox, safari).

    Returns:
        Session details with ID and remote debugging URL.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    if project_id is not None:
        validate_project_id(project_id)
    validate_browser(browser)

    body: JSONObject = {
        "headless": headless,
        "browser": browser,
    }

    if project_id is not None:
        body["projectId"] = project_id

    result = await request(HttpMethod.POST, "/sessions", body)
    return result


@tool(
    description="Get details of a browser session.",
    tags=["sessions", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def browserbase_get_session(
    session_id: str,
) -> JSONObject:
    """Get session details.

    Args:
        session_id: Session ID to retrieve.

    Returns:
        Session details including status and debugging URL.

    Raises:
        ValueError: If session_id is invalid.
        RuntimeError: If the API request fails.

    """
    validate_session_id(session_id)

    result = await request(HttpMethod.GET, f"/sessions/{session_id}")
    return result


@tool(
    description="List all browser sessions.",
    tags=["sessions", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def browserbase_list_sessions(
    limit: int = 20,
    offset: int = 0,
) -> JSONObject:
    """List all sessions.

    Args:
        limit: Number of results (1-100).
        offset: Pagination offset.

    Returns:
        List of sessions with pagination info.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_limit(limit)
    validate_offset(offset)

    result = await request(
        HttpMethod.GET, "/sessions", params={"limit": limit, "offset": offset}
    )
    return result


@tool(
    description="Get the recording of a browser session.",
    tags=["sessions", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def browserbase_get_session_recording(
    session_id: str,
) -> JSONObject:
    """Get session recording.

    Args:
        session_id: Session ID.

    Returns:
        Recording URL or data.

    Raises:
        ValueError: If session_id is invalid.
        RuntimeError: If the API request fails.

    """
    validate_session_id(session_id)

    result = await request(HttpMethod.GET, f"/sessions/{session_id}/recording")
    return result


@tool(
    description="Get logs from a browser session.",
    tags=["sessions", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def browserbase_get_session_logs(
    session_id: str,
) -> JSONObject:
    """Get session logs.

    Args:
        session_id: Session ID.

    Returns:
        Session logs with timestamps and messages.

    Raises:
        ValueError: If session_id is invalid.
        RuntimeError: If the API request fails.

    """
    validate_session_id(session_id)

    result = await request(HttpMethod.GET, f"/sessions/{session_id}/logs")
    return result


@tool(
    description="End a browser session.",
    tags=["sessions", "write"],
    annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True),
)
async def browserbase_end_session(
    session_id: str,
) -> JSONObject:
    """End a session.

    Args:
        session_id: Session ID to end.

    Returns:
        Confirmation of session termination.

    Raises:
        ValueError: If session_id is invalid.
        RuntimeError: If the API request fails.

    """
    validate_session_id(session_id)

    result = await request(HttpMethod.DELETE, f"/sessions/{session_id}")
    return result


session_tools = [
    browserbase_create_session,
    browserbase_get_session,
    browserbase_list_sessions,
    browserbase_get_session_recording,
    browserbase_get_session_logs,
    browserbase_end_session,
]