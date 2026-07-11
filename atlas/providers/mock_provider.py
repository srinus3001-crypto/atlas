"""
Mock Provider
Used until a real AI provider is connected.
"""

from atlas.core.logger import Logger
from atlas.providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

    def generate(self, prompt: str):

        Logger.info("Mock AI Provider responding")

        return f"""
Executive Summary:
AI Automation remains the strongest niche.

Recommended Niches:
- AI Automation
- AI Coding
- AI Productivity

Confidence: 95
"""
