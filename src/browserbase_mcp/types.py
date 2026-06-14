# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Browserbase API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class SessionInfo(BaseModel, frozen=True, slots=True):
    """Browser session info."""

    id: str | None = None
    status: str | None = None
    remote_debugging_url: str | None = None
    browser: str | None = None
    headless: bool | None = None
    project_id: str | None = None
    created_at: str | None = None


class SessionList(BaseModel, frozen=True, slots=True):
    """List of sessions."""

    sessions: list[SessionInfo] = Field(default_factory=list)
    total: int | None = None


class RecordingInfo(BaseModel, frozen=True, slots=True):
    """Session recording info."""

    url: str | None = None
    duration: int | None = None


class LogEntry(BaseModel, frozen=True, slots=True):
    """Single log entry."""

    timestamp: str | None = None
    level: str | None = None
    message: str | None = None


class LogsResponse(BaseModel, frozen=True, slots=True):
    """Session logs response."""

    logs: list[LogEntry] = Field(default_factory=list)


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]