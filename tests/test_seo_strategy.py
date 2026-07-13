from atlas.departments.marketing.employees.seo_strategist import (
    SEOStrategist,
)


def main():
    SEOStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nSEO Strategy Test Completed")


if __name__ == "__main__":
    main()
