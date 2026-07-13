"""
Competitor Analysis Prompt
"""

PROMPT = """
You are a Senior Competitive Intelligence Analyst.

Research competitors for the following topic:

{title}

Return ONLY valid JSON.

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
