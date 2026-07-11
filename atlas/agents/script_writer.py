"""
Script Writer
"""

from atlas.core.logger import Logger
from atlas.services.ai_service import AIService


class ScriptWriter:

    def execute(self, research_report):

        Logger.info("Script Writer generating content")

        prompt = f"""
Create a compelling YouTube script.

Executive Summary:
{research_report.executive_summary}

Recommended Niches:
{research_report.recommended_niches}
"""

        response = AIService().generate(prompt)

        return response
