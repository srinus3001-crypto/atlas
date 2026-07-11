"""
Title Writer
"""

from atlas.core.logger import Logger
from atlas.services.ai_service import AIService


class TitleWriter:

    def execute(self, research_report):

        Logger.info("Title Writer generating title")

        prompt = f"""
Generate ONE compelling YouTube title.

Executive Summary:
{research_report.executive_summary}

Audience:
{research_report.audience_segments}
"""

        return AIService().generate(prompt)
