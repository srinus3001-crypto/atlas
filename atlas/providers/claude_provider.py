"""
Claude Provider
Anthropic Claude Integration
"""

import os

from anthropic import Anthropic
from dotenv import load_dotenv

from atlas.core.logger import Logger
from atlas.core.settings import ai_settings
from atlas.providers.base_provider import BaseProvider


load_dotenv()


class ClaudeProvider(BaseProvider):

    def __init__(self):

        api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. Check your .env file."
            )

        self.client = Anthropic(api_key=api_key)

    def generate(self, prompt: str):

        Logger.info("Claude Provider invoked")

        response = self.client.messages.create(
            model=ai_settings.MODEL,
            max_tokens=ai_settings.MAX_TOKENS,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text_parts = []

        for block in response.content:

            if hasattr(block, "text"):
                text_parts.append(block.text)

        return "\n".join(text_parts)

