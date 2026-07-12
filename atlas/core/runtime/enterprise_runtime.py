"""
Atlas Enterprise Runtime

Central execution pipeline for Atlas Enterprise OS.
"""

from atlas.core.logger import Logger

from atlas.memory.memory_service import MemoryService

from atlas.core.runtime.plugin_pipeline import PluginPipeline


class EnterpriseRuntime:
    def __init__(self):
        self.memory = MemoryService()

        self.pipeline = PluginPipeline()

    def execute(
        self,
        context,
        employee,
    ):
        Logger.info("=" * 60)

        Logger.info("ENTERPRISE RUNTIME STARTED")

        Logger.info(f"Employee : {context.employee}")

        Logger.info(f"Department : {context.department}")

        Logger.info(f"Workspace : {context.workspace_id}")

        Logger.info("=" * 60)

        #
        # Load Workspace Memory
        #

        workspace_memory = self.memory.load(context.workspace_id)

        context.memory = workspace_memory.knowledge

        Logger.info(f"Memory Loaded ({len(context.memory)} knowledge items)")

        #
        # BEFORE plugins
        #

        self.pipeline.before_execute(
            context,
            employee,
        )

        #
        # Execute Employee
        #

        artifact = employee.execute(context)

        #
        # AFTER plugins
        #

        self.pipeline.after_execute(
            context,
            employee,
            artifact,
        )

        #
        # Update Enterprise Memory
        #

        self.memory.remember(
            context.workspace_id,
            employee.__class__.__name__,
            artifact,
        )

        Logger.info("Workspace Memory Updated")

        Logger.info("=" * 60)

        Logger.info("ENTERPRISE RUNTIME FINISHED")

        Logger.info("=" * 60)

        return artifact
