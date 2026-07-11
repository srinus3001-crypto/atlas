"""
Campaign
Primary business object for Atlas.
"""

from dataclasses import dataclass, field


@dataclass
class Campaign:

    campaign_id: str

    title: str

    business_goal: str

    target_revenue: str

    platforms: list = field(default_factory=list)

    research_report = None

    content_package = None

    publishing_plan = None

    analytics_report = None

    revenue_report = None

    status: str = "Planning"
