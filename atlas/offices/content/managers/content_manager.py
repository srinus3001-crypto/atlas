"""
Content Manager

Coordinates enterprise content generation.
"""

from atlas.core.logger import Logger
from atlas.prompts.content_director_prompt import ContentDirectorPrompt
from atlas.services.ai_service import AIService
from atlas.parsers.content_parser import ContentParser


class ContentManager:

    def execute(self, mission, research_report):

        Logger.info("Content Manager started")

        prompt = ContentDirectorPrompt.build(research_report)

        Logger.info("Submitting content request to Atlas AI")

        response = AIService().generate(
            task="content",
            prompt=prompt
        )

        Logger.info("Content received from Claude")

        package = ContentParser().parse(
            mission,
            response
        )

        Logger.info("Content Package Created")

        return package

