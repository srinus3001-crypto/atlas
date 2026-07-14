"""
Hook Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.hook_strategy import (
    HookStrategy,
)

from atlas.departments.content.prompts.hook_strategy_prompt import (
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


class HookStrategist(EnterpriseEmployee):
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
        return HookStrategy(
            workspace_id=workspace_id,
            opening_hooks=data["opening_hooks"],
            curiosity_hooks=data["curiosity_hooks"],
            emotional_hooks=data["emotional_hooks"],
            authority_hooks=data["authority_hooks"],
            contrarian_hooks=data["contrarian_hooks"],
            short_form_hooks=data["short_form_hooks"],
            long_form_hooks=data["long_form_hooks"],
            recommendations=data["recommendations"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "hook_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "hook_strategy"

    def report_type(
        self,
    ):
        return "HookStrategy"
