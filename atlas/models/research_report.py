"""
Research Report
Structured output from the Research Office.
"""

from dataclasses import dataclass, field


@dataclass
class ResearchReport:

    mission_id: str

    executive_summary: str

    recommended_niches: list = field(default_factory=list)

    competitors: list = field(default_factory=list)

    audience_segments: list = field(default_factory=list)

    opportunities: list = field(default_factory=list)

    risks: list = field(default_factory=list)

    action_plan: list = field(default_factory=list)

    confidence: int = 0
