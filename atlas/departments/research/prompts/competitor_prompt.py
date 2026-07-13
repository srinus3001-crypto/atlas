"""
Competitor Analysis Prompt
"""

PROMPT = """
You are a Competitive Intelligence Analyst.

Analyze competitors for:

{title}

Return ONLY valid JSON.

IMPORTANT:

- Maximum 5 direct competitors.
- Maximum 5 indirect competitors.
- Maximum 5 strengths.
- Maximum 5 weaknesses.
- Maximum 5 market gaps.
- Maximum 5 differentiation opportunities.
- Summary must be under 100 words.
- Do NOT include markdown.
- Do NOT include explanations.
- Return ONLY JSON.

{{
    "direct_competitors": [],
    "indirect_competitors": [],
    "competitor_strengths": [],
    "competitor_weaknesses": [],
    "market_gaps": [],
    "differentiation_opportunities": [],
    "summary": ""
}}
"""
