"""
Mission Evaluation

Evaluates mission success against predefined KPIs.
"""

from atlas.core.logger import Logger


class MissionEvaluation:

    def evaluate(self, metrics, actual):

        Logger.info("Evaluating mission")

        score = 0
        checks = 0

        if metrics.views_target:
            checks += 1
            if actual.get("views", 0) >= metrics.views_target:
                score += 1

        if metrics.ctr_target:
            checks += 1
            if actual.get("ctr", 0) >= metrics.ctr_target:
                score += 1

        if metrics.revenue_target:
            checks += 1
            if actual.get("revenue", 0) >= metrics.revenue_target:
                score += 1

        percentage = 0

        if checks:
            percentage = round(score / checks * 100, 2)

        return {
            "score": percentage,
            "passed": percentage >= 80
        }

