"""
Mission Launch Service
"""

import threading

from atlas.core.goal_manager import GoalManager
from atlas.offices.strategy_office import StrategyOffice
from atlas.strategy.mission_planner import MissionPlanner
from atlas.core.execution_engine import ExecutionEngine


class MissionLaunchService:
    def launch(self, goal_text):
        goal = GoalManager().create_demo_goal()

        goal.title = goal_text
        goal.objective = goal_text

        strategy = StrategyOffice().execute(goal)

        mission = MissionPlanner().plan(strategy)

        thread = threading.Thread(
            target=ExecutionEngine().execute,
            args=(mission,),
            daemon=True,
        )

        thread.start()

        return mission
