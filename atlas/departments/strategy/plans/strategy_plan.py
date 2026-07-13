"""
Strategy Plan
"""

from dataclasses import dataclass
from typing import List


@dataclass
class StrategyPlan:
    tasks: List[str]
