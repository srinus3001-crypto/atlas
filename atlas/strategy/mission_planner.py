"""
Mission Planner
"""

from atlas.core.id_generator import IDGenerator
from atlas.core.logger import Logger
from atlas.models.mission import Mission


class MissionPlanner:
    def plan(self, strategy):
        Logger.info("Mission Planner generating mission")

        mission = Mission(
            mission_id=IDGenerator().next_mission_id(),
            title="Build AI Media Company",
            objective="Generate ₹1 Lakh Monthly Profit",
            priority=strategy["priority"],
            owner_office=strategy["owner_office"],
        )

        Logger.info(f"Mission Planned : {mission.mission_id}")

        return mission
