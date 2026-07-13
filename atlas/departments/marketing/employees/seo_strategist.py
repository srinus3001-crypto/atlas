"""
SEO Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.marketing.models.seo_strategy import (
    SEOStrategy,
)

from atlas.departments.marketing.prompts.seo_prompt import (
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


class SEOStrategist(EnterpriseEmployee):
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
        return SEOStrategy(
            workspace_id=workspace_id,
            primary_keywords=data["primary_keywords"],
            secondary_keywords=data["secondary_keywords"],
            content_clusters=data["content_clusters"],
            on_page_strategy=data["on_page_strategy"],
            technical_seo=data["technical_seo"],
            link_building_strategy=data["link_building_strategy"],
            local_seo=data["local_seo"],
            measurement_metrics=data["measurement_metrics"],
            roadmap=data["roadmap"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        MarketingRepository().save(
            "seo_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "seo_strategy"

    def report_type(
        self,
    ):
        return "SEOStrategy"
