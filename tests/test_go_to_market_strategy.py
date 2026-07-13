"""
Go-To-Market Strategy Test
"""

from atlas.departments.strategy.employees.go_to_market_strategist import (
    GoToMarketStrategist,
)


def main():
    GoToMarketStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nGo-To-Market Strategy Test Completed")


if __name__ == "__main__":
    main()
