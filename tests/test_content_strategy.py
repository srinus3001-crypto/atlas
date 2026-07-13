from atlas.departments.marketing.employees.content_strategist import (
    ContentStrategist,
)


def main():
    ContentStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nContent Strategy Test Completed")


if __name__ == "__main__":
    main()
