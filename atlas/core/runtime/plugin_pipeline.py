"""
Atlas Plugin Pipeline

Executes all runtime plugins.
"""

from atlas.core.logger import Logger

from atlas.core.runtime.plugins import ArtifactPlugin


class PluginPipeline:
    def __init__(self):
        #
        # Plugin execution order
        #

        self.plugins = [
            ArtifactPlugin(),
        ]

    def before_execute(
        self,
        context,
        employee,
    ):
        for plugin in self.plugins:
            Logger.info(f"Plugin BEFORE : {plugin.__class__.__name__}")

            plugin.before_execute(
                context,
                employee,
            )

    def after_execute(
        self,
        context,
        employee,
        artifact,
    ):
        for plugin in self.plugins:
            Logger.info(f"Plugin AFTER : {plugin.__class__.__name__}")

            plugin.after_execute(
                context,
                employee,
                artifact,
            )
