from atlas.departments.marketing.employees.growth_strategist import (
    GrowthStrategist,
)


def main():
    GrowthStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nGrowth Strategy Test Completed")


if __name__ == "__main__":
    main()
