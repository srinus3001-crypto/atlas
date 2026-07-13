"""
Pricing Strategist
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.strategy.models.pricing_strategy import (
    PricingStrategy,
)

from atlas.departments.strategy.prompts.pricing_strategy_prompt import (
    PROMPT,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class PricingStrategist(EnterpriseEmployee):
    def task_name(self):
        return "pricing_strategy"

    def build_prompt(self, **kwargs):
        return PROMPT.format(
            title=kwargs["title"],
        )

    def build_report(self, data, **kwargs):
        return PricingStrategy(
            workspace_id=kwargs["workspace_id"],
            pricing_model=data["pricing_model"],
            pricing_tiers=data["pricing_tiers"],
            freemium_features=data["freemium_features"],
            premium_features=data["premium_features"],
            enterprise_offerings=data["enterprise_offerings"],
            discounts=data["discounts"],
            upsell_strategy=data["upsell_strategy"],
            annual_plan_benefits=data["annual_plan_benefits"],
            positioning=data["positioning"],
            summary=data["summary"],
        )

    def save(self, report):
        StrategyRepository().save(
            "pricing_strategy.json",
            report,
        )
