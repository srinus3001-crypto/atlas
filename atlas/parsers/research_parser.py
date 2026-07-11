"""
Research Parser
Converts AI output into a ResearchReport.
"""

from atlas.models.research_report import ResearchReport


class ResearchParser:

    def parse(self, mission, response):

        return ResearchReport(
            mission_id=mission.mission_id,
            executive_summary=response,
            recommended_niches=[],
            competitors=[],
            audience_segments=[],
            opportunities=[],
            risks=[],
            action_plan=[],
            confidence=90
        )
