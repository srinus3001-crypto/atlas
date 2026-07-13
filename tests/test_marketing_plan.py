"""
Marketing Plan Test
"""

from atlas.departments.marketing.employees.chief_marketing_officer import (
    ChiefMarketingOfficer,
)


def main():
    plan = ChiefMarketingOfficer().create_plan(
        title="AI replaces Software Engineers?",
    )

    print(plan)


if __name__ == "__main__":
    main()
