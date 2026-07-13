"""
Atlas Runtime Settings
"""


class AISettings:
    PROVIDER = "claude"

    MODEL = "claude-sonnet-5"

    MAX_TOKENS = 4000

    TEMPERATURE = 0.3


class RuntimeSettings:
    ENVIRONMENT = "Development"

    DEBUG = True

    LOG_LEVEL = "INFO"


ai_settings = AISettings()

runtime_settings = RuntimeSettings()
