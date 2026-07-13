"""
Campaign Strategy Test
"""

from atlas.departments.marketing.employees.campaign_strategist import (
    CampaignStrategist,
)


def main():

    CampaignStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nCampaign Strategy Test Completed")


if __name__ == "__main__":
    main()