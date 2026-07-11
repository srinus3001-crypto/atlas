"""
Success Metrics

Defines measurable outcomes for every Atlas mission.
"""

from dataclasses import dataclass


@dataclass
class SuccessMetrics:

    revenue_target: float = 0.0

    views_target: int = 0

    ctr_target: float = 0.0

    watch_time_target: float = 0.0

    conversion_target: float = 0.0

    quality_target: float = 90.0

