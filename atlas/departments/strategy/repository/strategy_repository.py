"""
Strategy Repository
"""

import json

from pathlib import Path
from dataclasses import asdict


class StrategyRepository:
    def __init__(self):
        self.root = Path("knowledge/workspaces")

    def _strategy_folder(
        self,
        workspace_id,
    ):
        folder = self.root / workspace_id / "strategy"

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
            self._strategy_folder(report.workspace_id) / filename,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                asdict(report),
                f,
                indent=4,
                ensure_ascii=False,
            )

    def load(
        self,
        filename,
        workspace_id,
    ):
        with open(
            self._strategy_folder(workspace_id) / filename,
            "r",
            encoding="utf-8",
        ) as f:
            return json.load(f)
