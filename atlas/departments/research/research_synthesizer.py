"""
Research Synthesizer

Chief Research Officer Executive Summary
"""

import json


from atlas.core.logger import Logger
from atlas.core.json.json_parser import JSONParser

from atlas.services.ai_service import AIService

from atlas.departments.research.models.research_summary import (
    ResearchSummary,
)

from atlas.departments.research.prompts.research_summary_prompt import (
    PROMPT,
)

from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)


class ResearchSynthesizer:
    def __init__(self):
        self.repository = ResearchRepository()

    def execute(
        self,
        workspace_id,
    ):
        Logger.info("Research Synthesizer Started")

        reports = {
            "market": self.repository.load(
                "market.json",
                workspace_id,
            ),
            "trends": self.repository.load(
                "trends.json",
                workspace_id,
            ),
            "audience": self.repository.load(
                "audience.json",
                workspace_id,
            ),
            "competitor": self.repository.load(
                "competitor.json",
                workspace_id,
            ),
            "seo": self.repository.load(
                "seo.json",
                workspace_id,
            ),
            "risk": self.repository.load(
                "risk.json",
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
            task="research_summary",
            prompt=prompt,
        )

        Logger.info("Research Summary AI response received")

        print("\n========== RAW SUMMARY RESPONSE ==========\n")
        print(response.content)
        print("\n==========================================\n")

        data = JSONParser.extract(
            response.content,
        )
        summary = ResearchSummary(
            workspace_id=workspace_id,
            executive_summary=data["executive_summary"],
            market_overview=data["market_overview"],
            audience_overview=data["audience_overview"],
            competitive_landscape=data["competitive_landscape"],
            seo_strategy=data["seo_strategy"],
            risk_assessment=data["risk_assessment"],
            strategic_recommendations=data["strategic_recommendations"],
            recommended_content=data["recommended_content"],
            business_score=data["business_score"],
            confidence=data["confidence"],
            recommendation=data["recommendation"],
        )

        self.repository.save_summary(
            summary,
        )

        Logger.info("Research Summary Saved")

        Logger.info("Research Synthesizer Finished")

        return summary
