"""Types for the tap-todoist package."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

type ConfigDict = Mapping[str, Any]
type StateDict = Mapping[str, Any]
