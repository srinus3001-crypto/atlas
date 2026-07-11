from atlas.models.mission import Mission
from atlas.models.mission_status import MissionStatus
from atlas.core.logger import Logger


class MissionManager:

    def create_demo_mission(self):

        mission = Mission(
            mission_id="M001",
            title="Build AI Media Company",
            objective="Generate ₹1 lakh/month",
            priority="HIGH",
            owner_office="Research"
        )

        Logger.info(f"Mission Created : {mission.mission_id}")

        return mission

    def validate(self, mission):

        mission.status = MissionStatus.VALIDATED

        Logger.info(
            f"Mission {mission.mission_id} -> {mission.status.value}"
        )

        return mission
