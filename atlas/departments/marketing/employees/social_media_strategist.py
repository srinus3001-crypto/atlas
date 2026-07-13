"""
Social Media Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.marketing.models.social_media_strategy import (
    SocialMediaStrategy,
)

from atlas.departments.marketing.prompts.social_media_strategy_prompt import (
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


class SocialMediaStrategist(EnterpriseEmployee):
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
        return SocialMediaStrategy(
            workspace_id=workspace_id,
            target_platforms=data["target_platforms"],
            content_mix=data["content_mix"],
            posting_schedule=data["posting_schedule"],
            campaign_ideas=data["campaign_ideas"],
            engagement_strategy=data["engagement_strategy"],
            influencer_strategy=data["influencer_strategy"],
            community_strategy=data["community_strategy"],
            kpis=data["kpis"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        MarketingRepository().save(
            "social_media_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "social_media_strategy"

    def report_type(
        self,
    ):
        return "SocialMediaStrategy"
