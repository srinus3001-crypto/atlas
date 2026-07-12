"""
Opportunity Model

Represents a business opportunity discovered by Atlas.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Opportunity:
    opportunity_id: str

    title: str

    niche: str

    source: str

    description: str

    trend_score: int

    revenue_score: int

    competition_score: int

    evergreen_score: int

    overall_score: int

    status: str = "Discovered"

    created_at: datetime = datetime.now()
