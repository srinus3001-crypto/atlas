"""
Strategy Summary
"""

from dataclasses import dataclass


@dataclass
class StrategySummary:
    workspace_id: str

    executive_summary: str = ""

    business_overview: str = ""

    revenue_strategy: str = ""

    product_strategy: str = ""

    pricing_strategy: str = ""

    go_to_market_strategy: str = ""

    strategic_recommendations: list = None

    risks: list = None

    next_steps: list = None
