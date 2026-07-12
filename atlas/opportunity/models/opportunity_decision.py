"""
Opportunity Decision
"""

from dataclasses import dataclass


@dataclass
class OpportunityDecision:
    approved: bool

    confidence: int

    reason: str

    priority: str
