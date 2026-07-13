"""
Strategy Synthesizer

Chief Strategy Officer Executive Summary
"""

import json

from atlas.core.logger import Logger
from atlas.core.json.json_parser import JSONParser

from atlas.services.ai_service import AIService

from atlas.departments.strategy.models.strategy_summary import (
    StrategySummary,
)

from atlas.departments.strategy.prompts.strategy_summary_prompt import (
    PROMPT,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class StrategySynthesizer:
    def __init__(self):
        self.repository = StrategyRepository()

    def execute(
        self,
        workspace_id,
    ):
        Logger.info("Strategy Synthesizer Started")

        reports = {
            "business_strategy": self.repository.load(
                "business_strategy.json",
                workspace_id,
            ),
            "revenue_strategy": self.repository.load(
                "revenue_strategy.json",
                workspace_id,
            ),
            "product_strategy": self.repository.load(
                "product_strategy.json",
                workspace_id,
            ),
            "pricing_strategy": self.repository.load(
                "pricing_strategy.json",
                workspace_id,
            ),
            "go_to_market_strategy": self.repository.load(
                "go_to_market_strategy.json",
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
            task="strategy_summary",
            prompt=prompt,
        )

        Logger.info("Strategy Summary AI response received")

        print("\n========== RAW STRATEGY SUMMARY ==========\n")
        print(response.content)
        print("\n==========================================\n")

        data = JSONParser.extract(
            response.content,
        )

        summary = StrategySummary(
            workspace_id=workspace_id,
            executive_summary=data["executive_summary"],
            business_overview=data["business_overview"],
            revenue_strategy=data["revenue_strategy"],
            product_strategy=data["product_strategy"],
            pricing_strategy=data["pricing_strategy"],
            go_to_market_strategy=data["go_to_market_strategy"],
            strategic_recommendations=data["strategic_recommendations"],
            risks=data["risks"],
            next_steps=data["next_steps"],
        )

        self.repository.save(
            "strategy_summary.json",
            summary,
        )

        Logger.info("Strategy Summary Saved")

        Logger.info("Strategy Synthesizer Finished")

        return summary
