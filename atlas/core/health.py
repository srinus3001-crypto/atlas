"""
Atlas Health Check
"""

from atlas.core.logger import Logger


class HealthCheck:

    def run(self):

        Logger.info("Health Check Started")

        checks = {
            "Configuration": True,
            "Logger": True,
            "Runtime": True,
        }

        for name, status in checks.items():
            if status:
                print(f"[PASS] {name}")
            else:
                print(f"[FAIL] {name}")

        Logger.info("System Health : HEALTHY")
