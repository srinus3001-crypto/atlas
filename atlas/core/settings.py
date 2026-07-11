"""
Atlas Runtime Settings
"""


class AISettings:

    PROVIDER = "claude"

    MODEL = "claude-sonnet-5"

    MAX_TOKENS = 2000

    TEMPERATURE = 0.7


class RuntimeSettings:

    ENVIRONMENT = "Development"

    DEBUG = True

    LOG_LEVEL = "INFO"


ai_settings = AISettings()

runtime_settings = RuntimeSettings()

