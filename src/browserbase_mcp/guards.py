# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Input validation for Browserbase API parameters."""

from __future__ import annotations

import re


# Browser/session ID: alphanumeric with hyphens/underscores
_ID_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$")


def validate_session_id(session_id: str) -> None:
    """Validate a session ID."""
    if not session_id or not _ID_RE.match(session_id):
        msg = f"Invalid session ID: {session_id!r}"
        raise ValueError(msg)


def validate_project_id(project_id: str) -> None:
    """Validate a project ID."""
    if not project_id or not _ID_RE.match(project_id):
        msg = f"Invalid project ID: {project_id!r}"
        raise ValueError(msg)


def validate_browser(browser: str) -> None:
    """Validate browser type."""
    valid_browsers = {"chrome", "firefox", "safari"}
    if browser not in valid_browsers:
        msg = f"Browser must be one of {valid_browsers}, got {browser}"
        raise ValueError(msg)


def validate_limit(limit: int) -> None:
    """Validate pagination limit."""
    if limit < 1 or limit > 100:
        msg = f"Limit must be between 1 and 100, got {limit}"
        raise ValueError(msg)


def validate_offset(offset: int) -> None:
    """Validate pagination offset."""
    if offset < 0:
        msg = f"Offset must be non-negative, got {offset}"
        raise ValueError(msg)