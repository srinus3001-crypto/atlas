"""
Audience Report
"""

from dataclasses import dataclass, field


@dataclass
class AudienceReport:
    workspace_id: str

    primary_audience: list = field(default_factory=list)

    secondary_audience: list = field(default_factory=list)

    pain_points: list = field(default_factory=list)

    motivations: list = field(default_factory=list)

    platforms: list = field(default_factory=list)

    search_intent: list = field(default_factory=list)

    recommended_tone: str = ""

    summary: str = ""
