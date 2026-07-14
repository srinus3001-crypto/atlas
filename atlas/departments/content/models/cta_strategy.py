"""
CTA Strategy
"""

from dataclasses import dataclass


@dataclass
class CTAStrategy:
    workspace_id: str

    primary_ctas: list

    secondary_ctas: list

    engagement_ctas: list

    newsletter_ctas: list

    community_ctas: list

    premium_ctas: list

    timing: list

    recommendations: list

    summary: str
