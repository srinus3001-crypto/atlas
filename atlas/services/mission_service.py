"""
Mission Service

Provides mission information to Atlas Studio.
"""

from pathlib import Path


class MissionService:
    def __init__(self):
        self.root = Path("knowledge/missions")

    def list_missions(self):
        if not self.root.exists():
            return []

        missions = []

        for folder in sorted(self.root.iterdir()):
            if folder.is_dir():
                missions.append(
                    {
                        "id": folder.name,
                        "status": (
                            "Completed"
                            if (folder / "research.md").exists()
                            and (folder / "content.md").exists()
                            else "Queued"
                        ),
                        "research": (folder / "research.md").exists(),
                        "content": (folder / "content.md").exists(),
                    }
                )

        return missions
