"""
Story Architecture
"""

from dataclasses import dataclass


@dataclass
class StoryArchitecture:
    workspace_id: str

    opening_scene: list

    story_flow: list

    curiosity_loops: list

    retention_checkpoints: list

    visual_cues: list

    b_roll: list

    transitions: list

    emotional_arc: list

    pacing: list

    ending: list

    recommendations: list

    summary: str
