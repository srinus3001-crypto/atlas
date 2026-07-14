"""
Content Synthesizer Test
"""

from atlas.departments.content.content_synthesizer import (
    ContentSynthesizer,
)


def main():
    ContentSynthesizer().execute(
        workspace_id="P001",
        title="AI replaces Software Engineers?",
    )

    print("\nContent Synthesizer Test Completed")


if __name__ == "__main__":
    main()
