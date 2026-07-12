"""
Research Service
"""

import json
from pathlib import Path


class ResearchService:
    def __init__(self):
        self.root = Path("knowledge/missions")

    def load_markdown(self, mission_id: str):
        file = self.root / mission_id / "research.md"

        if not file.exists():
            return "Research report not found."

        return file.read_text(encoding="utf-8")

    def load_json(self, mission_id: str):
        file = self.root / mission_id / "research.json"

        if not file.exists():
            return {}

        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
