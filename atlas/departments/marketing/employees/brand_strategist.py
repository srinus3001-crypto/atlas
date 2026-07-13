"""
Brand Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.marketing.models.brand_strategy import (
    BrandStrategy,
)

from atlas.departments.marketing.prompts.brand_prompt import (
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


class BrandStrategist(EnterpriseEmployee):
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

        return (
            PROMPT
            + "\n\n"
            + json.dumps(
                {
                    "title": title,
                    "research_summary": research,
                    "strategy_summary": strategy,
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
        return BrandStrategy(
            workspace_id=workspace_id,
            brand_vision=data["brand_vision"],
            brand_mission=data["brand_mission"],
            positioning=data["positioning"],
            target_audience=data["target_audience"],
            personality=data["personality"],
            brand_voice=data["brand_voice"],
            brand_promise=data["brand_promise"],
            messaging_pillars=data["messaging_pillars"],
            value_proposition=data["value_proposition"],
            brand_story=data["brand_story"],
            tagline_ideas=data["tagline_ideas"],
            differentiators=data["differentiators"],
            brand_guidelines=data["brand_guidelines"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        MarketingRepository().save(
            "brand_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "brand_strategy"

    def report_type(
        self,
    ):
        return "BrandStrategy"
