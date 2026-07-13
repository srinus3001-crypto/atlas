"""
Business Strategy
"""

from dataclasses import dataclass, field


@dataclass
class BusinessStrategy:
    workspace_id: str

    vision: str = ""

    mission: str = ""

    value_proposition: str = ""

    target_market: str = ""

    competitive_advantage: str = ""

    business_model: str = ""

    revenue_model: str = ""

    key_resources: list = field(default_factory=list)

    key_partnerships: list = field(default_factory=list)

    strategic_goals: list = field(default_factory=list)

    summary: str = ""
