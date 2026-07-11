"""
Content Office
"""

from atlas.core.logger import Logger
from atlas.models.work_package import WorkPackage
from atlas.offices.base_office import BaseOffice
from atlas.offices.content.managers.content_manager import ContentManager
from atlas.repository.artifact_writer import ArtifactWriter
from atlas.repository.mission_repository import MissionRepository
from atlas.models.research_report import ResearchReport


class ContentOffice(BaseOffice):

    def execute(self, mission):

        Logger.info("Content Office Started")

        repository = MissionRepository()

        research_data = repository.load_json(
            mission,
            "research.json"
        )

        if research_data is None:

            Logger.error("Research report not found")

            return WorkPackage(
                mission_id=mission.mission_id,
                office="Content",
                status="Failed",
                payload={
                    "error": "Missing research report"
                },
                next_office=None
            )

        Logger.info("Research Report Loaded")

        research = ResearchReport(**research_data)

        manager = ContentManager()

        package = manager.execute(
            mission,
            research
        )

        Logger.info("Saving Content Package")

        writer = ArtifactWriter()

        writer.repository.save_markdown(
            mission,
            "content.md",
            package.script
        )

        writer.repository.save_json(
            mission,
            "content.json",
            package.__dict__
        )

        Logger.info("Content Package Saved")

        return WorkPackage(
            mission_id=mission.mission_id,
            office="Content",
            status="Completed",
            payload={
                "content": package
            },
            next_office=None
        )

