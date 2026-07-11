"""
Research Service

Loads research artifacts for Atlas Studio.
"""

from pathlib import Path


class ResearchService:

    def load_markdown(self, mission_id):

        file = Path(
            f"knowledge/missions/{mission_id}/research.md"
        )

        if not file.exists():
            return "Research not found."

        return file.read_text(encoding="utf-8")