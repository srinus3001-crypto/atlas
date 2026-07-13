"""
Competitor Analyst
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.research.models.competitor_report import (
    CompetitorReport,
)

from atlas.departments.research.prompts.competitor_prompt import PROMPT

from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)


class CompetitorAnalyst(EnterpriseEmployee):
    def task_name(self):
        return "competitor"

    def build_prompt(self, **kwargs):
        return PROMPT.format(
            title=kwargs["title"],
        )

    def build_report(self, data, **kwargs):
        return CompetitorReport(
            workspace_id=kwargs["workspace_id"],
            direct_competitors=data["direct_competitors"],
            indirect_competitors=data["indirect_competitors"],
            competitor_strengths=data["competitor_strengths"],
            competitor_weaknesses=data["competitor_weaknesses"],
            market_gaps=data["market_gaps"],
            differentiation_opportunities=data["differentiation_opportunities"],
            summary=data["summary"],
        )

    def save(self, report):
        ResearchRepository().save(
            "competitor.json",
            report,
        )
