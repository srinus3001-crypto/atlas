"""
Chief Content Officer
"""

from atlas.departments.content.plans.content_plan import (
    ContentPlan,
)


class ChiefContentOfficer:
    def create_plan(
        self,
    ):
        return ContentPlan(
            tasks=[
                "Trend Intelligence",
                "Audience Psychology",
                "Topic Strategy",
                "Hook Strategy",
                "Script Strategy",
                "Story Architecture",
                "CTA Strategy",
            ]
        )
