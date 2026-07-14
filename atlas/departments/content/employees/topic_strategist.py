"""
Topic Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.topic_strategy import (
    TopicStrategy,
)

from atlas.departments.content.prompts.topic_strategy_prompt import (
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


class TopicStrategist(EnterpriseEmployee):
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

        trend = ContentRepository().load(
            "trend_analysis.json",
            workspace_id,
        )

        audience = ContentRepository().load(
            "audience_psychology.json",
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
            "trend_summary": trend.get(
                "summary",
                "",
            ),
            "audience_summary": audience.get(
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
        return TopicStrategy(
            workspace_id=workspace_id,
            priority_topics=data["priority_topics"],
            evergreen_topics=data["evergreen_topics"],
            trending_topics=data["trending_topics"],
            video_series=data["video_series"],
            content_calendar=data["content_calendar"],
            high_value_keywords=data["high_value_keywords"],
            recommended_formats=data["recommended_formats"],
            publishing_priority=data["publishing_priority"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "topic_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "topic_strategy"

    def report_type(
        self,
    ):
        return "TopicStrategy"
