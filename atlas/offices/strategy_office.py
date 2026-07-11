"""
Strategy Office
"""

from atlas.offices.base_office import BaseOffice
from atlas.core.logger import Logger
from atlas.offices.strategy.director import StrategyDirector


class StrategyOffice(BaseOffice):

    def execute(self, goal):

        Logger.info("Strategy Office Started")

        director = StrategyDirector()

        strategy = director.execute(goal)

        Logger.info("Enterprise Strategy Created")

        return strategy
