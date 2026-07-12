"""
Artifact Manager

Responsible for managing runtime artifacts.
"""

from atlas.core.logger import Logger


class ArtifactManager:
    def save(self, context, employee, artifact):
        context.artifacts[employee.__class__.__name__] = artifact

        Logger.info(f"Artifact stored: {employee.__class__.__name__}")

        return artifact
