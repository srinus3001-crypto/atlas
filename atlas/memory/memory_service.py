"""
Workspace Memory Service
"""

from datetime import datetime

from atlas.memory.memory_repository import MemoryRepository


class MemoryService:
    def __init__(self):
        self.repository = MemoryRepository()

    def load(self, workspace_id):
        return self.repository.load(workspace_id)

    def save(self, memory):
        memory.updated_at = datetime.utcnow().isoformat()

        self.repository.save(memory)

    def remember(self, workspace_id, category, value):
        memory = self.load(workspace_id)

        memory.knowledge[category] = value

        self.save(memory)

    def recall(self, workspace_id, category, default=None):
        memory = self.load(workspace_id)

        return memory.knowledge.get(category, default)
