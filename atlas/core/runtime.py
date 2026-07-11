"""
Atlas Runtime
"""

from atlas.core.logger import Logger
from atlas.core.health import HealthCheck
from atlas.core.goal_manager import GoalManager
from atlas.executive.ceo import CEO
from atlas.offices.strategy_office import StrategyOffice
from atlas.strategy.mission_planner import MissionPlanner
from atlas.core.mission_manager import MissionManager
from atlas.core.execution_engine import ExecutionEngine
from atlas.core.config import settings


class Runtime:

    def start(self):

        print("=" * 60)
        print(settings.SYSTEM_NAME)
        print(f"Version     : {settings.VERSION}")
        print(f"Environment : {settings.ENVIRONMENT}")
        print("=" * 60)

        Logger.info("Configuration Loaded")
        Logger.info("Runtime Started")

        HealthCheck().run()

        # Business Goal
        goal = GoalManager().create_demo_goal()

        # Executive Decision
        CEO().evaluate(goal)

        # Strategy
        strategy = StrategyOffice().execute(goal)

        # Mission Planning
        mission = MissionPlanner().plan(strategy)

        # Mission Validation
        mission = MissionManager().validate(mission)

        Logger.info(f"Current Stage : {mission.status.value}")

        # Execute
        ExecutionEngine().execute(mission)

        print("=" * 60)
        print("Atlas Ready")
        print("=" * 60)
