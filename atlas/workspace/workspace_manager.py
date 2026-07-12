"""
Workspace Manager

Creates enterprise workspaces.
"""

import json

from pathlib import Path
from dataclasses import asdict

from atlas.workspace.workspace import Workspace

from atlas.events.event import Event
from atlas.events.event_bus import event_bus
from atlas.events.event_types import EventTypes


class WorkspaceManager:
    def create(self, portfolio):
        workspace = Workspace(
            workspace_id=portfolio.portfolio_id,
            portfolio_id=portfolio.portfolio_id,
            title=portfolio.opportunity_title,
        )

        root = Path("knowledge/workspaces") / workspace.workspace_id

        root.mkdir(parents=True, exist_ok=True)

        folders = [
            "research",
            "competitors",
            "market",
            "scripts",
            "assets",
            "seo",
            "analytics",
            "publishing",
            "memory",
        ]

        for folder in folders:
            (root / folder).mkdir(exist_ok=True)

        with open(root / "workspace.json", "w", encoding="utf-8") as f:
            json.dump(asdict(workspace), f, indent=4, default=str)

        memory = {
            "portfolio": portfolio.opportunity_title,
            "knowledge": [],
            "lessons": [],
            "decisions": [],
        }

        with open(root / "memory.json", "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=4)

        event_bus.publish(
            Event(
                event_type=EventTypes.WORKSPACE_CREATED,
                entity_id=workspace.workspace_id,
                payload={
                    "workspace": workspace.workspace_id,
                    "portfolio": portfolio.portfolio_id,
                    "title": portfolio.opportunity_title,
                },
            )
        )

        return workspace
