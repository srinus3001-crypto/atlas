"""
Mission Status
"""

from enum import Enum


class MissionStatus(str, Enum):
    QUEUED = "Queued"
    RESEARCH = "Research"
    CONTENT = "Content"
    COMPLETED = "Completed"
    FAILED = "Failed"
