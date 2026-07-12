"""
Audience Analysis Prompt
"""

PROMPT = """
You are a senior Audience Research Analyst.

Analyse the topic:

{title}

Return ONLY valid JSON.

{{
  "primary_audience": [],
  "secondary_audience": [],
  "pain_points": [],
  "motivations": [],
  "platforms": [],
  "search_intent": [],
  "recommended_tone": "",
  "summary": ""
}}
"""
