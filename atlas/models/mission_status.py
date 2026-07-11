from enum import Enum


class MissionStatus(Enum):
    CREATED = "Created"
    VALIDATED = "Validated"
    PLANNED = "Planned"
    ASSIGNED = "Assigned"
    EXECUTING = "Executing"
    REVIEW = "Review"
    LEARNING = "Learning"
    COMPLETED = "Completed"
