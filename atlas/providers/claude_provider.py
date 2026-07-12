"""
Claude Provider

Anthropic Claude Integration
"""

import os

from anthropic import Anthropic
from dotenv import load_dotenv

from atlas.ai.ai_response import AIResponse
from atlas.core.logger import Logger
from atlas.core.settings import ai_settings
from atlas.providers.base_provider import BaseProvider

load_dotenv()


class ClaudeProvider(BaseProvider):
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found.")

        self.client = Anthropic(api_key=api_key)

    def generate(self, prompt: str):
        Logger.info("Claude Provider invoked")

        response = self.client.messages.create(
            model=ai_settings.MODEL,
            max_tokens=ai_settings.MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        text = ""

        for block in response.content:
            if hasattr(block, "text"):
                text += block.text

        text = text.strip()

        if text.startswith("```json"):
            text = text[7:]

        if text.startswith("```"):
            text = text[3:]

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        usage = getattr(response, "usage", None)

        input_tokens = 0
        output_tokens = 0

        if usage:
            input_tokens = getattr(
                usage,
                "input_tokens",
                0,
            )

            output_tokens = getattr(
                usage,
                "output_tokens",
                0,
            )

        return AIResponse(
            success=True,
            content=text,
            raw_text=text,
            model=ai_settings.MODEL,
            stop_reason=getattr(
                response,
                "stop_reason",
                "unknown",
            ),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
        )
