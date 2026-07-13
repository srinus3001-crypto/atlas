"""
Product Strategy Test
"""

from atlas.departments.strategy.employees.product_strategist import (
    ProductStrategist,
)


def main():
    ProductStrategist().execute(
        workspace_id="P001",
    )

    print("\nProduct Strategy Test Completed")


if __name__ == "__main__":
    main()
