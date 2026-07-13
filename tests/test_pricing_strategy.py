"""
Pricing Strategy Test
"""

from atlas.departments.strategy.employees.pricing_strategist import (
    PricingStrategist,
)


def main():
    PricingStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nPricing Strategy Test Completed")


if __name__ == "__main__":
    main()
