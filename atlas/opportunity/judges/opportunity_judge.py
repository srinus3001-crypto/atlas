"""
Opportunity Judge

Determines whether Atlas should invest
resources into an opportunity.
"""

from atlas.opportunity.models.opportunity_decision import OpportunityDecision


class OpportunityJudge:
    def evaluate(self, opportunity):
        score = opportunity.overall_score

        if score >= 85:
            return OpportunityDecision(
                approved=True,
                confidence=96,
                reason="High business value.",
                priority="High",
            )

        if score >= 75:
            return OpportunityDecision(
                approved=True,
                confidence=88,
                reason="Worth pursuing.",
                priority="Medium",
            )

        return OpportunityDecision(
            approved=False, confidence=82, reason="Low expected ROI.", priority="Low"
        )
