"""
Script Strategy Test
"""

from atlas.departments.content.employees.script_strategist import (
    ScriptStrategist,
)


def main():
    ScriptStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nScript Strategy Test Completed")


if __name__ == "__main__":
    main()
