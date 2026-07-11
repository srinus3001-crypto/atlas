"""
Audience Analyst
"""

from atlas.core.logger import Logger


class AudienceAnalyst:

    def execute(self, mission):

        Logger.info("Audience Analyst researching audience")

        return {
            "audience": [
                "Developers",
                "Business Owners",
                "Students",
                "Creators"
            ]
        }
