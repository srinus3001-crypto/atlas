"""
CTA Strategy Test
"""

from atlas.departments.content.employees.cta_strategist import (
    CTAStrategist,
)


def main():
    CTAStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nCTA Strategy Test Completed")


if __name__ == "__main__":
    main()
