"""
Campaign Manager
"""

from atlas.core.logger import Logger
from atlas.models.campaign import Campaign


class CampaignManager:

    def create_demo_campaign(self):

        Logger.info("Campaign Created : C001")

        return Campaign(
            campaign_id="C001",
            title="AI Automation for Professionals",
            business_goal="Generate ₹1 Lakh Monthly Revenue",
            target_revenue="₹100000/month",
            platforms=[
                "YouTube",
                "Instagram",
                "LinkedIn"
            ]
        )
