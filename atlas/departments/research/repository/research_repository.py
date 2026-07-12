"""
Research Repository
"""

import json

from pathlib import Path
from dataclasses import asdict


class ResearchRepository:
    def __init__(self):
        self.root = Path("knowledge/workspaces")

    def _research_folder(self, workspace_id):
        folder = self.root / workspace_id / "research"

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        return folder

    def save(
        self,
        filename,
        report,
    ):
        with open(
            self._research_folder(report.workspace_id) / filename,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                asdict(report),
                f,
                indent=4,
                ensure_ascii=False,
            )
