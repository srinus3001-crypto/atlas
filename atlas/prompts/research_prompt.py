"""
Research Prompt Builder
"""


class ResearchPrompt:

    @staticmethod
    def build(mission):

        return f"""
You are the Head of Research at Atlas.

Mission:
{mission.title}

Objective:
{mission.objective}

Return:

1. Executive Summary

2. Recommended Niches

3. Competitors

4. Audience

5. Opportunities

6. Risks

7. Action Plan

Return the response in structured JSON.
"""
