"""
Mission Status Service
"""

from pathlib import Path
import json


class StatusService:
    ROOT = Path("knowledge/status")

    def __init__(self):
        self.ROOT.mkdir(parents=True, exist_ok=True)

    def update(self, mission_id, stage, progress, message):
        data = {
            "mission": mission_id,
            "stage": stage,
            "progress": progress,
            "message": message,
        }

        with open(self.ROOT / f"{mission_id}.json", "w") as f:
            json.dump(data, f, indent=4)

    def load(self, mission_id):
        file = self.ROOT / f"{mission_id}.json"

        if not file.exists():
            return None

        with open(file) as f:
            return json.load(f)
