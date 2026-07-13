"""
Marketing Summary
"""

from dataclasses import dataclass


@dataclass
class MarketingSummary:
    workspace_id: str

    executive_summary: str

    brand_overview: str

    content_strategy: str

    seo_strategy: str

    social_media_strategy: str

    campaign_strategy: str

    growth_strategy: str

    strategic_recommendations: list

    key_metrics: list

    next_steps: list
