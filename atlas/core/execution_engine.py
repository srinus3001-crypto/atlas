"""
Execution Engine
"""

from atlas.models.mission_status import MissionStatus
from atlas.offices.research_office import ResearchOffice
from atlas.offices.content_office import ContentOffice
from atlas.services.status_service import StatusService


class ExecutionEngine:
    def __init__(self):
        self.status = StatusService()

    def execute(self, mission):
        print(f"[INFO] Execution Engine received mission {mission.mission_id}")

        try:
            # ----------------------------
            # Research Stage
            # ----------------------------
            mission.status = MissionStatus.RESEARCH

            self.status.update(
                mission.mission_id,
                "Research",
                25,
                "Research Office Started",
            )

            print("[INFO] Executing Office : Research")

            ResearchOffice().execute(mission)

            self.status.update(
                mission.mission_id,
                "Content",
                60,
                "Research Completed",
            )

            # ----------------------------
            # Content Stage
            # ----------------------------
            mission.status = MissionStatus.CONTENT

            self.status.update(
                mission.mission_id,
                "Content",
                75,
                "Content Office Started",
            )

            print("[INFO] Executing Office : Content")

            ContentOffice().execute(mission)

            # ----------------------------
            # Completed
            # ----------------------------
            mission.status = MissionStatus.COMPLETED

            self.status.update(
                mission.mission_id,
                "Completed",
                100,
                "Mission Completed",
            )

            print("[INFO] Mission Workflow Completed")

        except Exception as e:
            mission.status = MissionStatus.FAILED

            self.status.update(
                mission.mission_id,
                "Failed",
                100,
                str(e),
            )

            print(f"[ERROR] {e}")

            raise
