"""
Topic Strategy
"""

from dataclasses import dataclass


@dataclass
class TopicStrategy:
    workspace_id: str

    priority_topics: list

    evergreen_topics: list

    trending_topics: list

    video_series: list

    content_calendar: list

    high_value_keywords: list

    recommended_formats: list

    publishing_priority: list

    summary: str
