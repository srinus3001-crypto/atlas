"""
Audience Analyst
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.research.models.audience_report import AudienceReport
from atlas.departments.research.prompts.audience_prompt import PROMPT
from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)


class AudienceAnalyst(EnterpriseEmployee):
    def task_name(self):
        return "audience"

    def build_prompt(self, **kwargs):
        title = kwargs["title"]

        return PROMPT.format(
            title=title,
        )

    def build_report(self, data, **kwargs):
        return AudienceReport(
            workspace_id=kwargs["workspace_id"],
            primary_audience=data["primary_audience"],
            secondary_audience=data["secondary_audience"],
            pain_points=data["pain_points"],
            motivations=data["motivations"],
            platforms=data["platforms"],
            search_intent=data["search_intent"],
            recommended_tone=data["recommended_tone"],
            summary=data["summary"],
        )

    def save(self, report):
        ResearchRepository().save(
            "audience.json",
            report,
        )
