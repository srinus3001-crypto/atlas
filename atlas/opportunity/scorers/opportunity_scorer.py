"""
Opportunity Scorer
"""


class OpportunityScorer:
    def score(self, opportunity):
        score = (
            opportunity.trend_score * 0.35
            + opportunity.revenue_score * 0.35
            + (100 - opportunity.competition_score) * 0.15
            + opportunity.evergreen_score * 0.15
        )

        opportunity.overall_score = round(score)

        return opportunity
