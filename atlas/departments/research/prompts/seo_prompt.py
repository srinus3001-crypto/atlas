"""
SEO Analysis Prompt
"""

PROMPT = """
You are a Senior SEO Strategist.

Research SEO opportunities for:

{title}

Return ONLY valid JSON.

Limit every list to a maximum of 8 items.

Keep the summary under 120 words.

{{
    "primary_keywords": [],
    "long_tail_keywords": [],
    "high_intent_keywords": [],
    "content_clusters": [],
    "faq_questions": [],
    "featured_snippets": [],
    "internal_linking": [],
    "summary": ""
}}
"""
