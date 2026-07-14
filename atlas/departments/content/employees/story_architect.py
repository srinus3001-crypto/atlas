"""
Story Architect
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.content.models.story_architecture import (
    StoryArchitecture,
)

from atlas.departments.content.prompts.story_architecture_prompt import (
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


class StoryArchitect(EnterpriseEmployee):
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

        script = ContentRepository().load(
            "script_strategy.json",
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
            # Full script is needed by Story Architect
            "youtube_script": script.get(
                "youtube_script",
                "",
            ),
            "blog_outline": script.get(
                "blog_outline",
                [],
            ),
            "call_to_action": script.get(
                "call_to_action",
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
        return StoryArchitecture(
            workspace_id=workspace_id,
            opening_scene=data["opening_scene"],
            story_flow=data["story_flow"],
            curiosity_loops=data["curiosity_loops"],
            retention_checkpoints=data["retention_checkpoints"],
            visual_cues=data["visual_cues"],
            b_roll=data["b_roll"],
            transitions=data["transitions"],
            emotional_arc=data["emotional_arc"],
            pacing=data["pacing"],
            ending=data["ending"],
            recommendations=data["recommendations"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        ContentRepository().save(
            "story_architecture.json",
            report,
        )

    def task_name(
        self,
    ):
        return "story_architecture"

    def report_type(
        self,
    ):
        return "StoryArchitecture"
