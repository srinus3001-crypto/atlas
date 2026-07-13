"""
Product Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.strategy.models.product_strategy import (
    ProductStrategy,
)

from atlas.departments.strategy.prompts.product_strategy_prompt import (
    PROMPT,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class ProductStrategist(EnterpriseEmployee):
    def task_name(self):
        return "product_strategy"

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
        return ProductStrategy(
            workspace_id=kwargs["workspace_id"],
            core_product=data["core_product"],
            product_features=data["product_features"],
            unique_selling_points=data["unique_selling_points"],
            customer_problems=data["customer_problems"],
            roadmap=data["roadmap"],
            technology_stack=data["technology_stack"],
            competitive_positioning=data["competitive_positioning"],
            scalability_plan=data["scalability_plan"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        StrategyRepository().save(
            "product_strategy.json",
            report,
        )
