"""
Mission Plan

Represents an approved content assignment generated
from an opportunity.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class MissionPlan:
    mission_id: str

    title: str

    niche: str

    priority: str

    opportunity_score: int

    source: str

    channel: str

    content_type: str

    status: str = "Planned"

    created_at: datetime = field(default_factory=datetime.now)
