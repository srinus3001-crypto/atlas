"""
Research Plan
"""

from dataclasses import dataclass, field


@dataclass
class ResearchPlan:
    workspace_id: str

    title: str

    tasks: list = field(default_factory=list)
