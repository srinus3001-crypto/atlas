"""
Research Parser

Converts AI JSON into a ResearchReport.
"""

import json

from atlas.models.research_report import ResearchReport


class ResearchParser:
    def parse(self, mission, response):
        if isinstance(response, str):
            data = json.loads(response)
        else:
            data = response

        return ResearchReport(
            mission_id=mission.mission_id,
            executive_summary=data.get("executive_summary", ""),
            market_size=data.get("market_size", ""),
            audience_analysis=data.get("audience_analysis", ""),
            competitor_analysis=data.get("competitor_analysis", ""),
            top_opportunities=data.get("top_opportunities", ""),
            revenue_strategy=data.get("revenue_strategy", ""),
            risks=data.get("risks", ""),
            recommended_next_actions=data.get("recommended_next_actions", ""),
            recommended_niches=data.get("recommended_niches", []),
            competitors=data.get("competitors", []),
            audience_segments=data.get("audience_segments", []),
            opportunities=data.get("opportunities", []),
            action_plan=data.get("action_plan", []),
            confidence=data.get(
                "confidence",
                90,
            ),
        )
