"""
Pricing Strategy
"""

from dataclasses import dataclass, field


@dataclass
class PricingStrategy:
    workspace_id: str

    pricing_model: str = ""

    pricing_tiers: list = field(default_factory=list)

    freemium_features: list = field(default_factory=list)

    premium_features: list = field(default_factory=list)

    enterprise_offerings: list = field(default_factory=list)

    discounts: list = field(default_factory=list)

    upsell_strategy: list = field(default_factory=list)

    annual_plan_benefits: list = field(default_factory=list)

    positioning: str = ""

    summary: str = ""
