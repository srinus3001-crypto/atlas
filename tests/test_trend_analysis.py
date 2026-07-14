"""
Trend Analysis Test
"""

from atlas.departments.content.employees.trend_intelligence_analyst import (
    TrendIntelligenceAnalyst,
)


def main():
    TrendIntelligenceAnalyst().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nTrend Analysis Test Completed")


if __name__ == "__main__":
    main()
