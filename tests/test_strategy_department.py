"""
Strategy Department Test
"""

from atlas.departments.strategy.department import (
    StrategyDepartment,
)


def main():
    StrategyDepartment().execute(
        workspace_id="P001",
    )

    print("\nStrategy Department Test Completed")


if __name__ == "__main__":
    main()
