"""
CTA Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.cta_strategy import (
    CTAStrategy,
)

from atlas.departments.content.prompts.cta_strategy_prompt import (
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


class CTAStrategist(EnterpriseEmployee):
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

        script = ContentRepository().load(
            "script_strategy.json",
            workspace_id,
        )

        story = ContentRepository().load(
            "story_architecture.json",
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
            "script_summary": script.get(
                "summary",
                "",
            ),
            "story_summary": story.get(
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
        return CTAStrategy(
            workspace_id=workspace_id,
            primary_ctas=data["primary_ctas"],
            secondary_ctas=data["secondary_ctas"],
            engagement_ctas=data["engagement_ctas"],
            newsletter_ctas=data["newsletter_ctas"],
            community_ctas=data["community_ctas"],
            premium_ctas=data["premium_ctas"],
            timing=data["timing"],
            recommendations=data["recommendations"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "cta_strategy.json",
            report,
        )

    def task_name(
        self,
    ):
        return "cta_strategy"

    def report_type(
        self,
    ):
        return "CTAStrategy"
