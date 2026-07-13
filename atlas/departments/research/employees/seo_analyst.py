"""
SEO Analyst
"""

from atlas.core.employees.enterprise_employee import EnterpriseEmployee

from atlas.departments.research.models.seo_report import SEOReport

from atlas.departments.research.prompts.seo_prompt import PROMPT

from atlas.departments.research.repository.research_repository import (
    ResearchRepository,
)


class SEOAnalyst(EnterpriseEmployee):
    def task_name(self):
        return "seo"

    def build_prompt(self, **kwargs):
        return PROMPT.format(
            title=kwargs["title"],
        )

    def build_report(self, data, **kwargs):
        return SEOReport(
            workspace_id=kwargs["workspace_id"],
            primary_keywords=data["primary_keywords"],
            long_tail_keywords=data["long_tail_keywords"],
            high_intent_keywords=data["high_intent_keywords"],
            content_clusters=data["content_clusters"],
            faq_questions=data["faq_questions"],
            featured_snippets=data["featured_snippets"],
            internal_linking=data["internal_linking"],
            summary=data["summary"],
        )

    def save(self, report):
        ResearchRepository().save(
            "seo.json",
            report,
        )
