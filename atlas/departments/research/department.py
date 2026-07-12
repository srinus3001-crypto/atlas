"""
Research Department
"""

from atlas.core.logger import Logger

from atlas.departments.research.employees.chief_research_officer import (
    ChiefResearchOfficer,
)

from atlas.departments.research.employees.market_analyst import (
    MarketAnalyst,
)

from atlas.departments.research.employees.trend_analyst import (
    TrendAnalyst,
)

from atlas.departments.research.employees.audience_analyst import (
    AudienceAnalyst,
)


class ResearchDepartment:
    def execute(
        self,
        workspace_id,
        title,
    ):
        Logger.info("Research Department Started")

        plan = ChiefResearchOfficer().create_plan(
            workspace_id=workspace_id,
            title=title,
        )

        Logger.info(f"Research Plan contains {len(plan.tasks)} tasks")

        if "Market Analysis" in plan.tasks:
            MarketAnalyst().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Trend Analysis" in plan.tasks:
            TrendAnalyst().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Audience Analysis" in plan.tasks:
            AudienceAnalyst().execute(
                workspace_id=workspace_id,
                title=title,
            )

        Logger.info("Research Department Finished")
