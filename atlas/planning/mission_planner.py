"""
Mission Planner

Creates enterprise mission plans from approved opportunities.
"""

from atlas.core.logger import Logger
from atlas.core.id_generator import IDGenerator
from atlas.planning.mission_plan import MissionPlan


class MissionPlanner:
    def create(self, opportunity, decision):
        if not decision.approved:
            Logger.info(f"Rejected Opportunity : {opportunity.title}")
            return []

        Logger.info(f"Planning missions for : {opportunity.title}")

        plans = []

        plans.append(
            MissionPlan(
                mission_id=IDGenerator().next_mission_id(),
                title=opportunity.title,
                niche=opportunity.niche,
                priority=decision.priority,
                opportunity_score=opportunity.overall_score,
                source=opportunity.source,
                channel=opportunity.niche,
                content_type="YouTube Long Form",
            )
        )

        return plans
