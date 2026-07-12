"""
AI Response Model
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class AIResponse:
    success: bool

    content: Any

    raw_text: str

    model: str

    stop_reason: str

    input_tokens: int

    output_tokens: int

    total_tokens: int

    error: str | None = None
