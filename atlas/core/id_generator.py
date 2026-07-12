"""
Atlas ID Generator
"""

from pathlib import Path


class IDGenerator:
    def next_mission_id(self):
        root = Path("knowledge/missions")
        root.mkdir(parents=True, exist_ok=True)

        numbers = []

        for folder in root.iterdir():
            if folder.is_dir() and folder.name.startswith("M"):
                try:
                    numbers.append(int(folder.name[1:]))
                except ValueError:
                    pass

        if not numbers:
            return "M001"

        return f"M{max(numbers) + 1:03d}"
