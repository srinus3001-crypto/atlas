"""
Marketing Plan Generator
"""

from atlas.departments.marketing.models.marketing_plan import (
    MarketingPlan,
)


class MarketingPlanGenerator:
    def create(
        self,
        title,
    ):
        return MarketingPlan(
            tasks=[
                "Brand Strategy",
                "Content Strategy",
                "SEO Strategy",
                "Social Media Strategy",
                "Campaign Strategy",
                "Growth Strategy",
            ]
        )
