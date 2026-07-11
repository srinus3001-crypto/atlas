"""
AI Request

Represents a standardized request to Atlas AI.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class AIRequest:

    employee: Any

    mission: Any

    task: str

    instructions: str

    output_schema: str

