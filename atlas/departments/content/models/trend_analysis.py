"""
Trend Analysis
"""

from dataclasses import dataclass


@dataclass
class TrendAnalysis:
    workspace_id: str

    emerging_trends: list

    declining_trends: list

    evergreen_topics: list

    content_opportunities: list

    audience_interest: list

    opportunity_score: int

    trend_predictions: list

    recommendations: list

    summary: str
