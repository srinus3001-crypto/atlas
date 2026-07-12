"""
Atlas Event
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Event:
    event_type: str

    entity_id: str

    payload: dict

    timestamp: datetime = field(default_factory=datetime.utcnow)
