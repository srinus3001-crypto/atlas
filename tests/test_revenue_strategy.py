"""
Revenue Strategy Test
"""

from atlas.departments.strategy.employees.revenue_strategist import (
    RevenueStrategist,
)


def main():
    RevenueStrategist().execute(
        workspace_id="P001",
    )

    print("\nRevenue Strategy Test Completed")


if __name__ == "__main__":
    main()
