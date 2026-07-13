"""
Business Strategy Test
"""

from atlas.departments.strategy.employees.business_strategist import (
    BusinessStrategist,
)


def main():
    BusinessStrategist().execute(
        workspace_id="P001",
    )

    print("\nBusiness Strategy Test Completed")


if __name__ == "__main__":
    main()
