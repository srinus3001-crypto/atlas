"""
Story Architecture Test
"""

from atlas.departments.content.employees.story_architect import (
    StoryArchitect,
)


def main():
    StoryArchitect().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nStory Architecture Test Completed")


if __name__ == "__main__":
    main()
