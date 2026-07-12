"""
Research Listener

Automatically launches the Research Office
whenever a workspace is created.
"""

from atlas.core.logger import Logger

from atlas.events.event_bus import event_bus
from atlas.events.event_types import EventTypes

from atlas.models.mission import Mission
from atlas.offices.research_office import ResearchOffice


class ResearchListener:
    def __init__(self):
        event_bus.subscribe(EventTypes.WORKSPACE_CREATED, self.handle)

    def handle(self, event):
        Logger.info(f"Research Listener activated for {event.entity_id}")

        mission = Mission(
            mission_id=event.entity_id,
            title=event.payload["title"],
            objective=f"Research business opportunity: {event.payload['title']}",
            priority="Medium",
            owner_office="Research",
        )

        Logger.info("Launching Research Office...")

        ResearchOffice().execute(mission)

        Logger.info("Research Office completed.")


listener = ResearchListener()
