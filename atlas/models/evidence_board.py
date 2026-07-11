"""
Evidence Board
Shared evidence collected by research specialists.
"""

from dataclasses import dataclass, field


@dataclass
class EvidenceBoard:

    trend_findings: list = field(default_factory=list)

    competitor_findings: list = field(default_factory=list)

    audience_findings: list = field(default_factory=list)

    psychology_findings: list = field(default_factory=list)

    revenue_findings: list = field(default_factory=list)
