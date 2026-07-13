"""
Growth Strategy
"""

from dataclasses import dataclass


@dataclass
class GrowthStrategy:
    workspace_id: str

    acquisition_channels: list

    activation_strategy: list

    retention_strategy: list

    referral_strategy: list

    revenue_growth: list

    growth_experiments: list

    north_star_metric: str

    kpis: list

    roadmap: list

    summary: str
