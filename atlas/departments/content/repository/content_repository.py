"""
Content Repository
"""

import json
from dataclasses import asdict
from pathlib import Path


class ContentRepository:
    def _content_folder(
        self,
        workspace_id,
    ):
        folder = Path("knowledge") / "workspaces" / workspace_id / "content"

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
            self._content_folder(report.workspace_id) / filename,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                asdict(report),
                f,
                indent=2,
                ensure_ascii=False,
            )

    def load(
        self,
        filename,
        workspace_id,
    ):
        with open(
            self._content_folder(workspace_id) / filename,
            "r",
            encoding="utf-8",
        ) as f:
            return json.load(f)
