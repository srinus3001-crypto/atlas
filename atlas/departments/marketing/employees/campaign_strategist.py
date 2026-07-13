"""
Campaign Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.marketing.models.campaign_strategy import (
    CampaignStrategy,
)

from atlas.departments.marketing.prompts.campaign_strategy_prompt import (
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


class CampaignStrategist(EnterpriseEmployee):
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

        return (
            PROMPT
            + "\n\n"
            + json.dumps(
                {
                    "title": title,
                    "research_summary": research,
                    "strategy_summary": strategy,
                    "brand_strategy": brand,
                    "content_strategy": content,
                    "seo_strategy": seo,
                    "social_media_strategy": social,
                },
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
        return CampaignStrategy(
            workspace_id=workspace_id,
            campaign_objectives=data["campaign_objectives"],
            target_audience=data["target_audience"],
            campaign_types=data["campaign_types"],
            campaign_calendar=data["campaign_calendar"],
            channels=data["channels"],
            budget_allocation=data["budget_allocation"],
            success_metrics=data["success_metrics"],
            optimization_strategy=data["optimization_strategy"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        MarketingRepository().save(
            "campaign_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "campaign_strategy"

    def report_type(
        self,
    ):
        return "CampaignStrategy"
