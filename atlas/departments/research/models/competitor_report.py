"""
Competitor Report
"""

from dataclasses import dataclass, field


@dataclass
class CompetitorReport:
    workspace_id: str

    direct_competitors: list = field(default_factory=list)

    indirect_competitors: list = field(default_factory=list)

    competitor_strengths: list = field(default_factory=list)

    competitor_weaknesses: list = field(default_factory=list)

    market_gaps: list = field(default_factory=list)

    differentiation_opportunities: list = field(default_factory=list)

    summary: str = ""
