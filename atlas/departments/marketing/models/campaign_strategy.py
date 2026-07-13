"""
Campaign Strategy
"""

from dataclasses import dataclass


@dataclass
class CampaignStrategy:
    workspace_id: str

    campaign_objectives: list

    target_audience: list

    campaign_types: list

    campaign_calendar: list

    channels: list

    budget_allocation: list

    success_metrics: list

    optimization_strategy: list

    summary: str
