"""
Workspace Memory

Canonical enterprise memory model.

Every department stores knowledge here.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WorkspaceMemory:
    workspace_id: str

    knowledge: dict = field(default_factory=dict)

    artifacts: dict = field(default_factory=dict)

    facts: list = field(default_factory=list)

    lessons: list = field(default_factory=list)

    decisions: list = field(default_factory=list)

    history: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
