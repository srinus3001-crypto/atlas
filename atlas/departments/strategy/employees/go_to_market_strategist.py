"""
Go-To-Market Strategist
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.strategy.models.go_to_market_strategy import (
    GoToMarketStrategy,
)

from atlas.departments.strategy.prompts.go_to_market_strategy_prompt import (
    PROMPT,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class GoToMarketStrategist(EnterpriseEmployee):
    def task_name(self):
        return "go_to_market"

    def build_prompt(self, **kwargs):
        return PROMPT.format(
            title=kwargs["title"],
        )

    def build_report(self, data, **kwargs):
        return GoToMarketStrategy(
            workspace_id=kwargs["workspace_id"],
            target_segments=data["target_segments"],
            customer_personas=data["customer_personas"],
            acquisition_channels=data["acquisition_channels"],
            marketing_channels=data["marketing_channels"],
            sales_strategy=data["sales_strategy"],
            launch_strategy=data["launch_strategy"],
            partnerships=data["partnerships"],
            growth_loops=data["growth_loops"],
            key_metrics=data["key_metrics"],
            expansion_strategy=data["expansion_strategy"],
            summary=data["summary"],
        )

    def save(self, report):
        StrategyRepository().save(
            "go_to_market_strategy.json",
            report,
        )
