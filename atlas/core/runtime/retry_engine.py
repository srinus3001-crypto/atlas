"""
Enterprise Retry Engine
"""

from atlas.core.logger import Logger


class RetryEngine:
    MAX_RETRIES = 3

    @classmethod
    def execute(cls, operation):
        last_error = None

        attempts = 0

        for attempt in range(1, cls.MAX_RETRIES + 1):
            attempts = attempt

            try:
                Logger.info(f"Attempt {attempt}/{cls.MAX_RETRIES}")

                result = operation()

                return result, attempts

            except Exception as e:
                last_error = e

                Logger.info(f"Attempt {attempt} failed")

        raise last_error
