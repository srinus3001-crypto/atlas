"""
Chief Marketing Officer
"""

from atlas.core.logger import Logger

from atlas.departments.marketing.plans.marketing_plan import (
    MarketingPlanGenerator,
)


class ChiefMarketingOfficer:
    def create_plan(
        self,
        title,
    ):
        Logger.info("Chief Marketing Officer creating marketing plan")

        plan = MarketingPlanGenerator().create(
            title,
        )

        Logger.info(f"Marketing Plan contains {len(plan.tasks)} tasks")

        return plan
