"""
Risk Report
"""

from dataclasses import dataclass, field


@dataclass
class RiskReport:
    workspace_id: str

    technical_risks: list = field(default_factory=list)

    business_risks: list = field(default_factory=list)

    legal_risks: list = field(default_factory=list)

    copyright_risks: list = field(default_factory=list)

    platform_policy_risks: list = field(default_factory=list)

    ethical_considerations: list = field(default_factory=list)

    mitigation_strategies: list = field(default_factory=list)

    summary: str = ""
