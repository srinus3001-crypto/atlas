"""
Atlas Organizational Memory
"""

from atlas.core.logger import Logger


class MemoryRepository:

    def save(self, work_package):

        Logger.info(
            f"Knowledge Updated from {work_package.office} Office"
        )

        Logger.info(
            f"Mission {work_package.mission_id} archived"
        )
