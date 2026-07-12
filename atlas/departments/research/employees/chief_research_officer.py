"""
Chief Research Officer

Plans research activities for the department.
"""

from atlas.core.logger import Logger

from atlas.departments.research.models.research_plan import ResearchPlan


class ChiefResearchOfficer:
    def create_plan(self, workspace_id, title):
        Logger.info("Chief Research Officer creating research plan")

        return ResearchPlan(
            workspace_id=workspace_id,
            title=title,
            tasks=[
                "Market Analysis",
                "Trend Analysis",
                "Audience Analysis",
                "Competitor Analysis",
                "Risk Analysis",
            ],
        )
