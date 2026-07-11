"""
Hook Writer
"""

from atlas.core.logger import Logger
from atlas.services.ai_service import AIService


class HookWriter:

    def execute(self, research_report):

        Logger.info("Hook Writer generating hook")

        prompt = f"""
Write a powerful first 15-second hook.

Executive Summary:
{research_report.executive_summary}
"""

        return AIService().generate(prompt)
