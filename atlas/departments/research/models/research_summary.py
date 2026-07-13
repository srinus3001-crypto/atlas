"""
Research Summary
"""

from dataclasses import dataclass, field


@dataclass
class ResearchSummary:
    workspace_id: str

    executive_summary: str = ""

    market_overview: str = ""

    audience_overview: str = ""

    competitive_landscape: str = ""

    seo_strategy: str = ""

    risk_assessment: str = ""

    strategic_recommendations: list = field(default_factory=list)

    recommended_content: list = field(default_factory=list)

    business_score: int = 0

    confidence: int = 0

    recommendation: str = ""
