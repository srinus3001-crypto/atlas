"""
Hook Strategy Test
"""

from atlas.departments.content.employees.hook_strategist import (
    HookStrategist,
)


def main():
    HookStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nHook Strategy Test Completed")


if __name__ == "__main__":
    main()
