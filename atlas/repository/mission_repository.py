"""
Mission Repository

Stores and retrieves mission artifacts.
"""

from pathlib import Path
import json

from atlas.core.logger import Logger


class MissionRepository:

    ROOT = Path("knowledge/missions")

    def create(self, mission):

        mission_dir = self.ROOT / mission.mission_id
        mission_dir.mkdir(parents=True, exist_ok=True)

        return mission_dir

    def save_json(self, mission, filename, data):

        mission_dir = self.create(mission)

        path = mission_dir / filename

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        Logger.info(f"Saved {filename}")

    def save_markdown(self, mission, filename, content):

        mission_dir = self.create(mission)

        path = mission_dir / filename

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        Logger.info(f"Saved {filename}")

    def load_json(self, mission, filename):

        mission_dir = self.create(mission)

        path = mission_dir / filename

        if not path.exists():

            return None

        with open(path, "r", encoding="utf-8") as f:

            return json.load(f)

