"""
Research Manager

Coordinates enterprise market research.
"""

from atlas.core.logger import Logger
from atlas.services.ai_service import AIService
from atlas.parsers.research_parser import ResearchParser
from atlas.repository.artifact_writer import ArtifactWriter
from atlas.prompts.prompt_builder import PromptBuilder
from atlas.employees.employee_registry import EmployeeRegistry


class ResearchManager:

    def execute(self, mission):

        Logger.info("Research Manager started")

        employee = EmployeeRegistry.research_director()

        prompt = PromptBuilder.build(
            employee=employee,
            mission=mission,
            task="Research the assigned business opportunity.",
            instructions="""
Return ONLY valid JSON.

Do not use markdown.

Do not wrap the response in ```.

Schema:

{
  "executive_summary":"",
  "market_size":"",
  "audience_analysis":"",
  "competitor_analysis":"",
  "top_opportunities":"",
  "revenue_strategy":"",
  "risks":"",
  "recommended_next_actions":"",
  "confidence":95
}
"""
        )

        Logger.info("Submitting research request to Atlas AI")

        response = AIService().generate(
            task="research",
            prompt=prompt
        )

        Logger.info("Research received from Claude")

        report = ResearchParser().parse(
            mission,
            response
        )

        ArtifactWriter().save_research(
            mission,
            report
        )

        Logger.info("Research report generated")

        return report

