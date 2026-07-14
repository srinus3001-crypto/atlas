"""
Topic Strategy Test
"""

from atlas.departments.content.employees.topic_strategist import (
    TopicStrategist,
)


def main():
    TopicStrategist().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nTopic Strategy Test Completed")


if __name__ == "__main__":
    main()
