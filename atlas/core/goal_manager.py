"""
Goal Manager
"""

from atlas.core.logger import Logger
from atlas.models.business_goal import BusinessGoal


class GoalManager:

    def create_demo_goal(self):

        goal = BusinessGoal(
            goal_id="G001",
            title="Build AI Media Company",
            objective="Generate ₹1 Lakh Monthly Profit",
            priority="CRITICAL",
            target="31-Dec-2027"
        )

        Logger.info(f"Business Goal Created : {goal.goal_id}")

        return goal
