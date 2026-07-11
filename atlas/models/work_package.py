"""
Work Package
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class WorkPackage:
    mission_id: str
    office: str
    status: str
    payload: Any
    next_office: str | None = None
