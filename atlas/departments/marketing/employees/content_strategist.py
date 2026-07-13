"""
Content Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.marketing.models.content_strategy import (
    ContentStrategy,
)

from atlas.departments.marketing.prompts.content_prompt import (
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


class ContentStrategist(EnterpriseEmployee):
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

        return (
            PROMPT
            + "\n\n"
            + json.dumps(
                {
                    "title": title,
                    "research_summary": research,
                    "strategy_summary": strategy,
                    "brand_strategy": brand,
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
        return ContentStrategy(
            workspace_id=workspace_id,
            content_pillars=data["content_pillars"],
            content_formats=data["content_formats"],
            editorial_calendar=data["editorial_calendar"],
            publishing_frequency=data["publishing_frequency"],
            distribution_channels=data["distribution_channels"],
            content_funnel=data["content_funnel"],
            content_themes=data["content_themes"],
            engagement_strategy=data["engagement_strategy"],
            content_metrics=data["content_metrics"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        MarketingRepository().save(
            "content_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "content_strategy"

    def report_type(
        self,
    ):
        return "ContentStrategy"
