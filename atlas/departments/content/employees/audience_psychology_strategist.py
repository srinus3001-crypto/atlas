"""
Audience Psychology Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.audience_psychology import (
    AudiencePsychology,
)

from atlas.departments.content.prompts.audience_psychology_prompt import (
    PROMPT,
)

from atlas.departments.content.repository.content_repository import (
    ContentRepository,
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


class AudiencePsychologyStrategist(EnterpriseEmployee):

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
        return AudiencePsychology(
            workspace_id=workspace_id,
            primary_audience=data["primary_audience"],
            secondary_audience=data["secondary_audience"],
            pain_points=data["pain_points"],
            dream_outcomes=data["dream_outcomes"],
            fears=data["fears"],
            motivations=data["motivations"],
            emotional_triggers=data["emotional_triggers"],
            curiosity_triggers=data["curiosity_triggers"],
            viewing_triggers=data["viewing_triggers"],
            sharing_triggers=data["sharing_triggers"],
            objections=data["objections"],
            content_preferences=data["content_preferences"],
            platform_preferences=data["platform_preferences"],
            recommendations=data["recommendations"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "audience_psychology.json",
            report,
        )

    def task_name(
        self,
    ):
        return "audience_psychology"

    def report_type(
        self,
    ):
        return "AudiencePsychology"