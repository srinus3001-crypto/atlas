"""
Mission Model
"""

from dataclasses import dataclass
from atlas.models.mission_status import MissionStatus


@dataclass
class Mission:
    mission_id: str

    title: str

    objective: str

    priority: str

    owner_office: str

    status: MissionStatus = MissionStatus.QUEUED
