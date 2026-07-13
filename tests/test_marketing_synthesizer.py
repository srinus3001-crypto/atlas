"""
Marketing Synthesizer Test
"""

from atlas.departments.marketing.marketing_synthesizer import (
    MarketingSynthesizer,
)


def main():
    MarketingSynthesizer().execute(
        workspace_id="P001",
    )

    print("\nMarketing Synthesizer Test Completed")


if __name__ == "__main__":
    main()
