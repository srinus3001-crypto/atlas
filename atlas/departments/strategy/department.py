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

from atlas.departments.strategy.employees.pricing_strategist import (
    PricingStrategist,
)

from atlas.departments.strategy.employees.go_to_market_strategist import (
    GoToMarketStrategist,
)

from atlas.departments.strategy.strategy_synthesizer import (
    StrategySynthesizer,
)


class StrategyDepartment:
    def execute(
        self,
        workspace_id,
        title,
    ):
        Logger.info("Strategy Department Started")

        plan = ChiefStrategyOfficer().create_plan(
            title,
        )

        if "Business Strategy" in plan.tasks:
            BusinessStrategist().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Revenue Strategy" in plan.tasks:
            RevenueStrategist().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Product Strategy" in plan.tasks:
            ProductStrategist().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Pricing Strategy" in plan.tasks:
            PricingStrategist().execute(
                workspace_id=workspace_id,
                title=title,
            )

        if "Go-To-Market Strategy" in plan.tasks:
            GoToMarketStrategist().execute(
                workspace_id=workspace_id,
                title=title,
            )

        StrategySynthesizer().execute(
            workspace_id=workspace_id,
        )

        Logger.info("Strategy Department Finished")
