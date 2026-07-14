"""
Content Synthesizer
"""

import json

from atlas.core.logger import Logger
from atlas.services.ai_service import AIService
from atlas.core.json.json_parser import JSONParser

from atlas.departments.content.models.content_summary import (
    ContentSummary,
)

from atlas.departments.content.prompts.content_summary_prompt import (
    PROMPT,
)

from atlas.departments.content.repository.content_repository import (
    ContentRepository,
)


class ContentSynthesizer:
    def execute(
        self,
        workspace_id,
        title,
    ):
        Logger.info("Content Synthesizer Started")

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

        story = ContentRepository().load(
            "story_architecture.json",
            workspace_id,
        )

        cta = ContentRepository().load(
            "cta_strategy.json",
            workspace_id,
        )

        payload = {
            "title": title,
            "trend_analysis": trend,
            "audience_psychology": audience,
            "topic_strategy": topic,
            "hook_strategy": hook,
            "script_strategy": script,
            "story_architecture": story,
            "cta_strategy": cta,
        }

        response = AIService().generate(
            task="content_summary",
            prompt=PROMPT
            + "\n\n"
            + json.dumps(
                payload,
                indent=2,
                ensure_ascii=False,
            ),
        )

        Logger.info("Content Summary AI response received")

        print("\n========== RAW CONTENT SUMMARY ==========\n")

        print(response.content)

        print("\n=========================================\n")

        data = JSONParser.extract(
            response.content,
        )

        report = ContentSummary(
            workspace_id=workspace_id,
            executive_summary=data["executive_summary"],
            trend_summary=data["trend_summary"],
            audience_summary=data["audience_summary"],
            topic_summary=data["topic_summary"],
            hook_summary=data["hook_summary"],
            script_summary=data["script_summary"],
            story_summary=data["story_summary"],
            cta_summary=data["cta_summary"],
            strategic_recommendations=data["strategic_recommendations"],
            publishing_checklist=data["publishing_checklist"],
            next_steps=data["next_steps"],
        )

        ContentRepository().save(
            "content_summary.json",
            report,
        )

        Logger.info("Content Summary Saved")

        Logger.info("Content Synthesizer Finished")

        return report
