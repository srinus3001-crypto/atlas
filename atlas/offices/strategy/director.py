"""
Strategy Director
"""

from atlas.core.logger import Logger


class StrategyDirector:

    def execute(self, goal):

        Logger.info("Strategy Director evaluating CEO decision")

        return {
            "strategy": "Market Expansion",
            "owner_office": "Research",
            "priority": goal.priority
        }
