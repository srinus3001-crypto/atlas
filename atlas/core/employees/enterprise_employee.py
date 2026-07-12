"""
Enterprise Employee
"""

from datetime import datetime

from atlas.core.logger import Logger
from atlas.services.ai_service import AIService
from atlas.core.json.json_parser import JSONParser
from atlas.core.runtime.retry_engine import RetryEngine
from atlas.core.metrics.execution_metrics import ExecutionMetrics


class EnterpriseEmployee:
    def execute(self, **kwargs):
        Logger.info(f"{self.__class__.__name__} started")

        started = datetime.now()

        def operation():
            prompt = self.build_prompt(**kwargs)

            response = AIService().generate(task=self.task_name(), prompt=prompt)

            Logger.info(f"{self.__class__.__name__} AI response received")

            data = JSONParser.extract(response.content)

            report = self.build_report(data, **kwargs)

            self.save(report)

            return report

        report, attempts = RetryEngine.execute(operation)

        finished = datetime.now()

        metrics = ExecutionMetrics(
            employee=self.__class__.__name__,
            started_at=started,
            finished_at=finished,
            duration_seconds=(finished - started).total_seconds(),
            attempts=attempts,
            success=True,
        )

        Logger.info(
            f"{metrics.employee} completed in "
            f"{metrics.duration_seconds:.2f}s "
            f"(Attempts: {metrics.attempts})"
        )

        return report

    def task_name(self):
        raise NotImplementedError

    def build_prompt(self, **kwargs):
        raise NotImplementedError

    def build_report(self, data, **kwargs):
        raise NotImplementedError

    def save(self, report):
        raise NotImplementedError
