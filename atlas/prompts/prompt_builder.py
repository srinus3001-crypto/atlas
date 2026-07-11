"""
Prompt Builder

Builds enterprise prompts for every Atlas employee.
"""

from atlas.constitution.constitution import AtlasConstitution


class PromptBuilder:

    @staticmethod
    def build(
        employee,
        mission,
        task,
        instructions
    ):

        constitution = "\n".join(
            f"- {rule}"
            for rule in AtlasConstitution.CORE_PRINCIPLES
        )

        responsibilities = "\n".join(
            f"- {item}"
            for item in employee.responsibilities
        )

        return f"""
You are {employee.title}.

Company:
{AtlasConstitution.COMPANY_NAME}

Mission:
{AtlasConstitution.MISSION}

Vision:
{AtlasConstitution.VISION}

----------------------------------------

ATLAS CONSTITUTION

{constitution}

----------------------------------------

EMPLOYEE

Name:
{employee.name}

Department:
{employee.department}

Responsibilities:

{responsibilities}

Authority:

{employee.authority}

----------------------------------------

MISSION

Title:
{mission.title}

Objective:
{mission.objective}

Priority:
{mission.priority}

----------------------------------------

TASK

{task}

----------------------------------------

INSTRUCTIONS

{instructions}

Return a professional executive-quality response.

"""
