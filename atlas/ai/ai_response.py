"""
AI Response
"""

from dataclasses import dataclass


@dataclass
class AIResponse:

    success: bool

    raw_response: str

    parsed_data: dict | None = None

    tokens_used: int = 0

    model: str = ""

    error: str = ""

