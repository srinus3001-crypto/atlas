"""
Content Portfolio

Represents a collection of content generated
from one business opportunity.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ContentPortfolio:
    portfolio_id: str

    opportunity_title: str

    niche: str

    source: str

    priority: str

    score: int

    research_required: bool = True

    status: str = "Planned"

    created_at: datetime = field(default_factory=datetime.now)
