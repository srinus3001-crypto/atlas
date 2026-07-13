"""
Strategy Synthesizer Test
"""

from atlas.departments.strategy.strategy_synthesizer import (
    StrategySynthesizer,
)


def main():
    StrategySynthesizer().execute(
        workspace_id="P001",
    )

    print("\nStrategy Synthesizer Test Completed")


if __name__ == "__main__":
    main()
