"""
Research Office
"""

from atlas.offices.base_office import BaseOffice
from atlas.core.logger import Logger
from atlas.offices.research.director import ResearchDirector
from atlas.models.work_package import WorkPackage


class ResearchOffice(BaseOffice):

    def execute(self, mission):

        Logger.info("Research Office Started")

        director = ResearchDirector()

        result = director.execute(mission)

        Logger.info(f"Research Director Decision : {result['status']}")

        return WorkPackage(
            mission_id=mission.mission_id,
            office="Research",
            status="Completed",
            payload={
                "director": result,
                "summary": "Initial research completed"
            },
            next_office="Content"
        )
