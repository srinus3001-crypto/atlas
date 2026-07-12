"""
Enterprise Execution Metrics
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExecutionMetrics:
    employee: str

    started_at: datetime

    finished_at: datetime

    duration_seconds: float

    attempts: int

    success: bool
