"""
Risk Analyst
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.research.models.risk_report import RiskReport
from atlas.departments.research.prompts.risk_prompt import PROMPT
from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)


class RiskAnalyst(EnterpriseEmployee):
    def task_name(self):
        return "risk"

    def build_prompt(self, **kwargs):
        return PROMPT.format(
            title=kwargs["title"],
        )

    def build_report(self, data, **kwargs):
        return RiskReport(
            workspace_id=kwargs["workspace_id"],
            technical_risks=data["technical_risks"],
            business_risks=data["business_risks"],
            legal_risks=data["legal_risks"],
            copyright_risks=data["copyright_risks"],
            platform_policy_risks=data["platform_policy_risks"],
            ethical_considerations=data["ethical_considerations"],
            mitigation_strategies=data["mitigation_strategies"],
            summary=data["summary"],
        )

    def save(self, report):
        ResearchRepository().save(
            "risk.json",
            report,
        )
