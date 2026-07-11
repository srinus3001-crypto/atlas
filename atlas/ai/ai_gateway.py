"""
AI Gateway

Enterprise entry point for all Atlas AI requests.
"""

from atlas.core.logger import Logger
from atlas.ai.ai_response import AIResponse
from atlas.prompts.prompt_builder import PromptBuilder
from atlas.services.ai_service import AIService


class AIGateway:

    def execute(self, request):

        Logger.info("AI Gateway started")

        prompt = PromptBuilder.build(
            employee=request.employee,
            mission=request.mission,
            task=request.task,
            instructions=request.instructions
        )

        Logger.info("Prompt constructed")

        raw_response = AIService().generate(
            task=request.task,
            prompt=prompt
        )

        Logger.info("AI response received")

        return AIResponse(
            success=True,
            raw_response=raw_response,
            model="claude-sonnet-5"
        )

