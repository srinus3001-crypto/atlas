"""
Atlas Enterprise Runtime Context

Carries execution state across the runtime.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RuntimeContext:
    workspace_id: str

    employee: str

    department: str

    title: str

    artifacts: dict = field(default_factory=dict)

    memory: dict = field(default_factory=dict)

    metrics: dict = field(default_factory=dict)

    events: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    started_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
