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

from atlas.departments.research.employees.competitor_analyst import (
    CompetitorAnalyst,
)

from atlas.departments.research.employees.seo_analyst import (
    SEOAnalyst,
)

from atlas.departments.research.employees.risk_analyst import (
    RiskAnalyst,
)

from atlas.departments.research.research_synthesizer import (
    ResearchSynthesizer,
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

        if "Competitor Analysis" in plan.tasks:
            CompetitorAnalyst().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "SEO Analysis" in plan.tasks:
            SEOAnalyst().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Risk Analysis" in plan.tasks:
            RiskAnalyst().execute(
                workspace_id=workspace_id,
                title=title,
            )

        Logger.info("Generating Executive Research Summary")

        ResearchSynthesizer().execute(
            workspace_id=workspace_id,
        )

        Logger.info("Research Department Finished")
