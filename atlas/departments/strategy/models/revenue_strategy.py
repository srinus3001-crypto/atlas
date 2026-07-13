"""
Revenue Strategy
"""

from dataclasses import dataclass, field


@dataclass
class RevenueStrategy:
    workspace_id: str

    revenue_streams: list = field(default_factory=list)

    pricing_model: str = ""

    customer_segments: list = field(default_factory=list)

    acquisition_channels: list = field(default_factory=list)

    lifetime_value_strategy: str = ""

    monetization_timeline: str = ""

    projected_revenue: str = ""

    risks: list = field(default_factory=list)

    summary: str = ""
