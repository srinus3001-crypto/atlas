"""
Artifact Plugin
"""

from atlas.core.logger import Logger
from atlas.core.runtime.plugins.runtime_plugin import RuntimePlugin
from atlas.core.runtime.managers import ArtifactManager


class ArtifactPlugin(RuntimePlugin):
    def __init__(self):
        self.manager = ArtifactManager()

    def after_execute(
        self,
        context,
        employee,
        artifact,
    ):
        self.manager.save(
            context,
            employee,
            artifact,
        )

        Logger.info("Artifact Plugin Completed")
