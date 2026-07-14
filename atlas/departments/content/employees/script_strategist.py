"""
Script Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.script_strategy import (
    ScriptStrategy,
)

from atlas.departments.content.prompts.script_strategy_prompt import (
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


class ScriptStrategist(EnterpriseEmployee):
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

        topic = ContentRepository().load(
            "topic_strategy.json",
            workspace_id,
        )

        hook = ContentRepository().load(
            "hook_strategy.json",
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
            "topic_summary": topic.get(
                "summary",
                "",
            ),
            "hook_summary": hook.get(
                "summary",
                "",
            ),
            # Structured intelligence (better than summaries)
            "priority_topics": topic.get(
                "priority_topics",
                [],
            ),
            "video_series": topic.get(
                "video_series",
                [],
            ),
            "opening_hooks": hook.get(
                "opening_hooks",
                [],
            ),
            "curiosity_hooks": hook.get(
                "curiosity_hooks",
                [],
            ),
            "authority_hooks": hook.get(
                "authority_hooks",
                [],
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
        return ScriptStrategy(
            workspace_id=workspace_id,
            youtube_script=data["youtube_script"],
            linkedin_post=data["linkedin_post"],
            x_thread=data["x_thread"],
            newsletter=data["newsletter"],
            blog_outline=data["blog_outline"],
            call_to_action=data["call_to_action"],
            keywords=data["keywords"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "script_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "script_strategy"

    def report_type(
        self,
    ):
        return "ScriptStrategy"
