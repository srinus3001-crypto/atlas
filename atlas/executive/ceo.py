"""
Atlas CEO
Executive decision maker.
"""

from atlas.core.logger import Logger


class CEO:

    def evaluate(self, goal):

        Logger.info("CEO evaluating business goal")

        decision = {
            "approved": True,
            "priority": goal.priority,
            "strategy": "Market Expansion",
            "reason": "Goal aligns with enterprise vision"
        }

        Logger.info("CEO approved business goal")

        return decision
