"""
Atlas Workspace
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Workspace:
    workspace_id: str

    portfolio_id: str

    title: str

    status: str = "Active"

    created_at: datetime = field(default_factory=datetime.now)
