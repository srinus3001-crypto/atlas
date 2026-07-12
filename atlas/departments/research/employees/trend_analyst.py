"""
Trend Analyst
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.research.models.trend_report import TrendReport
from atlas.departments.research.repository.research_repository import ResearchRepository


class TrendAnalyst(EnterpriseEmployee):
    def task_name(self):
        return "trend"

    def build_prompt(self, **kwargs):
        title = kwargs["title"]

        return f"""
You are the Trend Analyst.

Research ONLY trends.

Return ONLY valid JSON.

{{
    "trending_topics": [],
    "search_trends": [],
    "viral_opportunities": [],
    "recommended_content": []
}}

Business:

{title}
"""

    def build_report(self, data, **kwargs):
        return TrendReport(
            workspace_id=kwargs["workspace_id"],
            trending_topics=data["trending_topics"],
            search_trends=data["search_trends"],
            viral_opportunities=data["viral_opportunities"],
            recommended_content=data["recommended_content"],
        )

    def save(self, report):
        ResearchRepository().save_trend_report(report)
