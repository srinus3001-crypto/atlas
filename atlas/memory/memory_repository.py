"""
Workspace Memory Repository
"""

import json

from pathlib import Path
from dataclasses import asdict

from atlas.memory.workspace_memory import WorkspaceMemory


class MemoryRepository:
    def __init__(self):
        self.root = Path("knowledge/workspaces")

    def _memory_file(self, workspace_id):
        folder = self.root / workspace_id

        folder.mkdir(parents=True, exist_ok=True)

        return folder / "memory.json"

    def save(self, memory):
        with open(self._memory_file(memory.workspace_id), "w", encoding="utf-8") as f:
            json.dump(asdict(memory), f, indent=4, ensure_ascii=False)

    def load(self, workspace_id):
        file = self._memory_file(workspace_id)

        if not file.exists():
            memory = WorkspaceMemory(workspace_id=workspace_id)

            self.save(memory)

            return memory

        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return self._migrate(workspace_id, data)

    def _migrate(self, workspace_id, data):
        """
        Automatically migrate older memory schemas
        to the latest WorkspaceMemory schema.
        """

        memory = WorkspaceMemory(workspace_id=workspace_id)

        if isinstance(data.get("knowledge"), dict):
            memory.knowledge = data["knowledge"]

        elif isinstance(data.get("knowledge"), list):
            memory.knowledge = {}

        memory.artifacts = data.get("artifacts", {})

        memory.facts = data.get("facts", [])

        memory.lessons = data.get("lessons", [])

        memory.decisions = data.get("decisions", [])

        memory.history = data.get("history", [])

        memory.metadata = data.get("metadata", {})

        if "portfolio" in data:
            memory.metadata["portfolio"] = data["portfolio"]

        self.save(memory)

        return memory
