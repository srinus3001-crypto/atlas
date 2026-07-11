"""
Research Director

Responsible for governance, review and approval
of enterprise research.
"""

from atlas.core.logger import Logger
from atlas.offices.research.managers.research_manager import ResearchManager


class ResearchDirector:

    def execute(self, mission):

        Logger.info("Research Director reviewing mission")

        manager = ResearchManager()

        report = manager.execute(mission)

        Logger.info("Research Director approved research")

        return {
            "status": "Ready",
            "report": report
        }

