"""
Brand Strategy Test
"""

from atlas.departments.marketing.employees.brand_strategist import (
    BrandStrategist,
)


def main():
    BrandStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nBrand Strategy Test Completed")


if __name__ == "__main__":
    main()
