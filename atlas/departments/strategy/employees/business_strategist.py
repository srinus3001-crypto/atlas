"""
Business Strategist
"""

import json

from atlas.core.employees.enterprise_employee import (
    EnterpriseEmployee,
)

from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)

from atlas.departments.strategy.models.business_strategy import (
    BusinessStrategy,
)

from atlas.departments.strategy.prompts.business_strategy_prompt import (
    PROMPT,
)

from atlas.departments.strategy.repository.strategy_repository import (
    StrategyRepository,
)


class BusinessStrategist(EnterpriseEmployee):
    def task_name(self):
        return "business_strategy"

    def build_prompt(self, **kwargs):
        research = ResearchRepository().load(
            "research_summary.json",
            kwargs["workspace_id"],
        )

        return PROMPT.format(
            research=json.dumps(
                research,
                indent=2,
                ensure_ascii=False,
            )
        )

    def build_report(
        self,
        data,
        **kwargs,
    ):
        return BusinessStrategy(
            workspace_id=kwargs["workspace_id"],
            vision=data["vision"],
            mission=data["mission"],
            value_proposition=data["value_proposition"],
            target_market=data["target_market"],
            competitive_advantage=data["competitive_advantage"],
            business_model=data["business_model"],
            revenue_model=data["revenue_model"],
            key_resources=data["key_resources"],
            key_partnerships=data["key_partnerships"],
            strategic_goals=data["strategic_goals"],
            summary=data["summary"],
        )

    def save(
        self,
        report,
    ):
        StrategyRepository().save(
            "business_strategy.json",
            report,
        )
