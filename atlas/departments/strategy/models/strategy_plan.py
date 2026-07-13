"""
Strategy Plan
"""

from dataclasses import dataclass, field


@dataclass
class StrategyPlan:
    tasks: list = field(default_factory=list)
