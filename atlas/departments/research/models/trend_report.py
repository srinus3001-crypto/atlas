"""
Trend Report
"""

from dataclasses import dataclass


@dataclass
class TrendReport:
    workspace_id: str

    trending_topics: list

    search_trends: list

    viral_opportunities: list

    recommended_content: list
