"""
Strategy Department
"""

from atlas.core.logger import Logger

from atlas.departments.strategy.employees.chief_strategy_officer import (
    ChiefStrategyOfficer,
)

from atlas.departments.strategy.employees.business_strategist import (
    BusinessStrategist,
)

from atlas.departments.strategy.employees.revenue_strategist import (
    RevenueStrategist,
)

from atlas.departments.strategy.employees.product_strategist import (
    ProductStrategist,
)


class StrategyDepartment:
    def execute(
        self,
        workspace_id,
    ):
        Logger.info("Strategy Department Started")

        plan = ChiefStrategyOfficer().create_plan(
            workspace_id=workspace_id,
        )

        Logger.info(f"Strategy Plan contains {len(plan.tasks)} tasks")

        if "Business Strategy" in plan.tasks:
            BusinessStrategist().execute(
                workspace_id=workspace_id,
            )

        if "Revenue Strategy" in plan.tasks:
            RevenueStrategist().execute(
                workspace_id=workspace_id,
            )

        if "Product Strategy" in plan.tasks:
            ProductStrategist().execute(
                workspace_id=workspace_id,
            )

        Logger.info("Strategy Department Finished")
