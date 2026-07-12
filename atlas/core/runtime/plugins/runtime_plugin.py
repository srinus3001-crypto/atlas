"""
Runtime Plugin Base Class

Every runtime plugin inherits from this class.
"""


class RuntimePlugin:
    def before_execute(
        self,
        context,
        employee,
    ):
        """
        Called before employee execution.
        """
        pass

    def after_execute(
        self,
        context,
        employee,
        artifact,
    ):
        """
        Called after employee execution.
        """
        pass
