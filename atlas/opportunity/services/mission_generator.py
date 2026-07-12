"""
Mission Generator

Creates missions from approved opportunities.
"""

from atlas.core.logger import Logger


class MissionGenerator:
    def create(self, opportunity, decision):
        if not decision.approved:
            Logger.info(f"Rejected Opportunity : {opportunity.title}")

            return None

        Logger.info(f"Mission Approved : {opportunity.title}")

        mission = {
            "title": opportunity.title,
            "niche": opportunity.niche,
            "priority": decision.priority,
            "score": opportunity.overall_score,
            "source": opportunity.source,
        }

        return mission
