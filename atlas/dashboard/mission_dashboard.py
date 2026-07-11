"""
Mission Dashboard

Displays mission status for Atlas Enterprise.
"""

from atlas.core.logger import Logger


class MissionDashboard:

    def show(self, mission, stages):

        Logger.info("Mission Dashboard")

        print()

        print("=" * 70)
        print("ATLAS ENTERPRISE OPERATING SYSTEM".center(70))
        print("=" * 70)

        print(f"Mission ID : {mission.mission_id}")
        print(f"Title      : {mission.title}")
        print(f"Priority   : {mission.priority}")
        print(f"Status     : {mission.status.value}")

        print()

        print("-" * 70)

        for stage in stages:

            icon = "✓" if stage["completed"] else "○"

            print(f"{icon} {stage['name']}")

        print("-" * 70)

        completed = sum(
            1 for s in stages if s["completed"]
        )

        progress = round(
            completed / len(stages) * 100
        )

        print(f"Mission Progress : {progress}%")

        print("=" * 70)

