"""
Base Office
"""

from abc import ABC, abstractmethod


class BaseOffice(ABC):

    @abstractmethod
    def execute(self, mission):
        """
        Execute a mission.
        """
        pass
