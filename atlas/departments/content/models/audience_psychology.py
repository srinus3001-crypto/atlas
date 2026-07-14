"""
Audience Psychology
"""

from dataclasses import dataclass


@dataclass
class AudiencePsychology:
    workspace_id: str

    primary_audience: list

    secondary_audience: list

    pain_points: list

    dream_outcomes: list

    fears: list

    motivations: list

    emotional_triggers: list

    curiosity_triggers: list

    viewing_triggers: list

    sharing_triggers: list

    objections: list

    content_preferences: list

    platform_preferences: list

    recommendations: list

    summary: str
