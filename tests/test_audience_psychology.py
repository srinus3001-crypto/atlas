"""
Audience Psychology Test
"""

from atlas.departments.content.employees.audience_psychology_strategist import (
    AudiencePsychologyStrategist,
)


def main():
    AudiencePsychologyStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nAudience Psychology Test Completed")


if __name__ == "__main__":
    main()
