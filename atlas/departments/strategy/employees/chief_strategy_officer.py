"""
Chief Strategy Officer
"""

from atlas.core.logger import Logger

from atlas.departments.strategy.models.strategy_plan import (
    StrategyPlan,
)


class ChiefStrategyOfficer:
    def create_plan(
        self,
        workspace_id,
    ):
        Logger.info("Chief Strategy Officer creating strategy plan")

        return StrategyPlan(
            tasks=[
                "Business Strategy",
                "Revenue Strategy",
                "Product Strategy",
                "Pricing Strategy",
                "Go-To-Market Strategy",
            ]
        )
