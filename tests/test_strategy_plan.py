from atlas.departments.strategy.employees.chief_strategy_officer import (
    ChiefStrategyOfficer,
)


def main():
    plan = ChiefStrategyOfficer().create_plan(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print(plan)


if __name__ == "__main__":
    main()
