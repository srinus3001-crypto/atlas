"""
Marketing Synthesizer

Chief Marketing Officer Executive Summary
"""

import json

from atlas.core.logger import Logger
from atlas.core.json.json_parser import JSONParser

from atlas.services.ai_service import AIService

from atlas.departments.marketing.models.marketing_summary import (
    MarketingSummary,
)

from atlas.departments.marketing.prompts.marketing_summary_prompt import (
    PROMPT,
)

from atlas.departments.marketing.repository.marketing_repository import (
    MarketingRepository,
)


class MarketingSynthesizer:
    def __init__(self):
        self.repository = MarketingRepository()

    def execute(
        self,
        workspace_id,
    ):
        Logger.info("Marketing Synthesizer Started")

        reports = {
            "brand": self.repository.load(
                "brand_strategy.json",
                workspace_id,
            ),
            "content": self.repository.load(
                "content_strategy.json",
                workspace_id,
            ),
            "seo": self.repository.load(
                "seo_strategy.json",
                workspace_id,
            ),
            "social_media": self.repository.load(
                "social_media_strategy.json",
                workspace_id,
            ),
            "campaign": self.repository.load(
                "campaign_strategy.json",
                workspace_id,
            ),
            "growth": self.repository.load(
                "growth_strategy.json",
                workspace_id,
            ),
        }

        prompt = (
            PROMPT
            + "\n\n"
            + json.dumps(
                reports,
                indent=2,
                ensure_ascii=False,
            )
        )

        response = AIService().generate(
            task="marketing_summary",
            prompt=prompt,
        )

        Logger.info("Marketing Summary AI response received")

        print("\n========== RAW MARKETING SUMMARY ==========\n")
        print(response.content)
        print("\n==========================================\n")

        data = JSONParser.extract(
            response.content,
        )

        summary = MarketingSummary(
            workspace_id=workspace_id,
            executive_summary=data["executive_summary"],
            brand_overview=data["brand_overview"],
            content_strategy=data["content_strategy"],
            seo_strategy=data["seo_strategy"],
            social_media_strategy=data["social_media_strategy"],
            campaign_strategy=data["campaign_strategy"],
            growth_strategy=data["growth_strategy"],
            strategic_recommendations=data["strategic_recommendations"],
            key_metrics=data["key_metrics"],
            next_steps=data["next_steps"],
        )

        self.repository.save(
            "marketing_summary.json",
            summary,
        )

        Logger.info("Marketing Summary Saved")
        Logger.info("Marketing Synthesizer Finished")

        return summary
