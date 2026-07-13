"""
Content Strategy
"""

from dataclasses import dataclass


@dataclass
class ContentStrategy:
    workspace_id: str

    content_pillars: list

    content_formats: list

    editorial_calendar: list

    publishing_frequency: str

    distribution_channels: list

    content_funnel: list

    content_themes: list

    engagement_strategy: list

    content_metrics: list

    summary: str
