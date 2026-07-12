"""
Trend Collector

Temporary mock collector.

Live sources will be added later.
"""

from atlas.opportunity.models.opportunity import Opportunity


class TrendCollector:
    def collect(self):
        return [
            Opportunity(
                opportunity_id="O001",
                title="AI replaces Software Engineers?",
                niche="AI",
                source="Mock",
                description="Trending discussion around AI replacing coding jobs.",
                trend_score=96,
                revenue_score=91,
                competition_score=62,
                evergreen_score=74,
                overall_score=0,
            ),
            Opportunity(
                opportunity_id="O002",
                title="Will Gold hit ₹1 Lakh?",
                niche="Finance",
                source="Mock",
                description="Finance discussion around gold investment.",
                trend_score=89,
                revenue_score=95,
                competition_score=58,
                evergreen_score=83,
                overall_score=0,
            ),
            Opportunity(
                opportunity_id="O003",
                title="Best AI Tools of 2026",
                niche="AI Education",
                source="Mock",
                description="AI productivity tools comparison.",
                trend_score=94,
                revenue_score=92,
                competition_score=51,
                evergreen_score=88,
                overall_score=0,
            ),
        ]
