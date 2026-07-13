"""
Risk Analysis Prompt
"""

PROMPT = """
You are a Chief Risk Officer.

Analyze all possible risks related to:

{title}

Return ONLY valid JSON.

Limit every list to a maximum of 8 items.

Keep the summary under 120 words.

{{
    "technical_risks": [],
    "business_risks": [],
    "legal_risks": [],
    "copyright_risks": [],
    "platform_policy_risks": [],
    "ethical_considerations": [],
    "mitigation_strategies": [],
    "summary": ""
}}
"""
