"""
Social Media Strategy
"""

from dataclasses import dataclass


@dataclass
class SocialMediaStrategy:
    workspace_id: str

    target_platforms: list

    content_mix: list

    posting_schedule: list

    campaign_ideas: list

    engagement_strategy: list

    influencer_strategy: list

    community_strategy: list

    kpis: list

    summary: str
