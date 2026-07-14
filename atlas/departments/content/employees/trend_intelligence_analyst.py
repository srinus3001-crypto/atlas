"""
Trend Intelligence Analyst
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.trend_analysis import (
    TrendAnalysis,
)

from atlas.departments.content.prompts.trend_analysis_prompt import (
    PROMPT,
)

from atlas.departments.content.repository.content_repository import (
    ContentRepository,
)

from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)

from atlas.departments.marketing.repository.marketing_repository import (
    MarketingRepository,
)


class TrendIntelligenceAnalyst(EnterpriseEmployee):
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

        marketing = MarketingRepository().load(
            "marketing_summary.json",
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
            "marketing_summary": marketing.get(
                "executive_summary",
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
        return TrendAnalysis(
            workspace_id=workspace_id,
            emerging_trends=data["emerging_trends"],
            declining_trends=data["declining_trends"],
            evergreen_topics=data["evergreen_topics"],
            content_opportunities=data["content_opportunities"],
            audience_interest=data["audience_interest"],
            opportunity_score=data["opportunity_score"],
            trend_predictions=data["trend_predictions"],
            recommendations=data["recommendations"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "trend_analysis.json",
            report,
        )

    def task_name(
        self,
    ):
        return "trend_analysis"

    def report_type(
        self,
    ):
        return "TrendAnalysis"
