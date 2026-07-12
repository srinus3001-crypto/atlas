"""
Market Report
"""

from dataclasses import dataclass


@dataclass
class MarketReport:
    workspace_id: str

    market_size: str

    growth_rate: str

    maturity: str

    opportunities: list
