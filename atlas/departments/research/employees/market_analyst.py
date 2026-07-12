"""
Market Analyst
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.research.models.market_report import MarketReport
from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)


class MarketAnalyst(EnterpriseEmployee):
    def task_name(self):
        return "market"

    def build_prompt(self, **kwargs):
        title = kwargs["title"]

        return f"""
You are the Market Analyst.

Research ONLY the market.

Return ONLY valid JSON.

{{
    "market_size":"",
    "growth_rate":"",
    "maturity":"",
    "opportunities":[]
}}

Business:

{title}
"""

    def build_report(self, data, **kwargs):
        return MarketReport(
            workspace_id=kwargs["workspace_id"],
            market_size=data["market_size"],
            growth_rate=data["growth_rate"],
            maturity=data["maturity"],
            opportunities=data["opportunities"],
        )

    def save(self, report):
        ResearchRepository().save(
            "market.json",
            report,
        )
