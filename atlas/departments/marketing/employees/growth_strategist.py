"""
Growth Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.marketing.models.growth_strategy import (
    GrowthStrategy,
)

from atlas.departments.marketing.prompts.growth_strategy_prompt import (
    PROMPT,
)

from atlas.departments.marketing.repository.marketing_repository import (
    MarketingRepository,
)

from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class GrowthStrategist(EnterpriseEmployee):
    def build_prompt(
        self,
        workspace_id,
        title,
    ):
        research = ResearchRepository().load(
            "research_summary.json",
            workspace_id,
        )

        strategy = StrategyRepository().load(
            "strategy_summary.json",
            workspace_id,
        )

        brand = MarketingRepository().load(
            "brand_strategy.json",
            workspace_id,
        )

        content = MarketingRepository().load(
            "content_strategy.json",
            workspace_id,
        )

        seo = MarketingRepository().load(
            "seo_strategy.json",
            workspace_id,
        )

        social = MarketingRepository().load(
            "social_media_strategy.json",
            workspace_id,
        )

        campaign = MarketingRepository().load(
            "campaign_strategy.json",
            workspace_id,
        )

        payload = {
            "title": title,
            "research_summary": research.get(
                "executive_summary",
                "",
            ),
            "strategy_summary": strategy.get(
                "executive_summary",
                "",
            ),
            "brand_summary": brand.get(
                "summary",
                "",
            ),
            "content_summary": content.get(
                "summary",
                "",
            ),
            "seo_summary": seo.get(
                "summary",
                "",
            ),
            "social_summary": social.get(
                "summary",
                "",
            ),
            "campaign_summary": campaign.get(
                "summary",
                "",
            ),
        }

        return (
            PROMPT
            + "\n\n"
            + json.dumps(
                payload,
                indent=2,
                ensure_ascii=False,
            )
        )

    def build_report(
        self,
        data,
        workspace_id,
        **kwargs,
    ):
        return GrowthStrategy(
            workspace_id=workspace_id,
            acquisition_channels=data["acquisition_channels"],
            activation_strategy=data["activation_strategy"],
            retention_strategy=data["retention_strategy"],
            referral_strategy=data["referral_strategy"],
            revenue_growth=data["revenue_growth"],
            growth_experiments=data["growth_experiments"],
            north_star_metric=data["north_star_metric"],
            kpis=data["kpis"],
            roadmap=data["roadmap"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        MarketingRepository().save(
            "growth_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "growth_strategy"

    def report_type(
        self,
    ):
        return "GrowthStrategy"
