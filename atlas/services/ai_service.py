"""
Atlas AI Service
"""

from atlas.core.logger import Logger
from atlas.core.settings import ai_settings

from atlas.providers.mock_provider import MockProvider
from atlas.providers.claude_provider import ClaudeProvider


class AIService:
    def __init__(self):
        if ai_settings.PROVIDER == "mock":
            self.provider = MockProvider()

        elif ai_settings.PROVIDER == "claude":
            self.provider = ClaudeProvider()

        else:
            raise ValueError(f"Unsupported AI Provider: {ai_settings.PROVIDER}")

    def generate(self, task: str, prompt: str):
        Logger.info(f"AI Service using provider: {ai_settings.PROVIDER}")

        return self.provider.generate(prompt)
