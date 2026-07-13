"""
Revenue Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.strategy.models.revenue_strategy import (
    RevenueStrategy,
)

from atlas.departments.strategy.prompts.revenue_strategy_prompt import (
    PROMPT,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class RevenueStrategist(EnterpriseEmployee):
    def task_name(self):
        return "revenue_strategy"

    def build_prompt(self, **kwargs):
        business = StrategyRepository().load(
            "business_strategy.json",
            kwargs["workspace_id"],
        )

        return PROMPT.format(
            business=json.dumps(
                business,
                indent=2,
                ensure_ascii=False,
            )
        )

    def build_report(
        self,
        data,
        **kwargs,
    ):
        return RevenueStrategy(
            workspace_id=kwargs["workspace_id"],
            revenue_streams=data["revenue_streams"],
            pricing_model=data["pricing_model"],
            customer_segments=data["customer_segments"],
            acquisition_channels=data["acquisition_channels"],
            lifetime_value_strategy=data["lifetime_value_strategy"],
            monetization_timeline=data["monetization_timeline"],
            projected_revenue=data["projected_revenue"],
            risks=data["risks"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        StrategyRepository().save(
            "revenue_strategy.json",
            report,
        )
