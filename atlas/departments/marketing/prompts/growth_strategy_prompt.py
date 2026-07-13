"""
Growth Strategy Prompt
"""

PROMPT = """
You are the Chief Growth Strategist.

Using the summaries below:

- Research Summary
- Strategy Summary
- Brand Summary
- Content Summary
- SEO Summary
- Social Media Summary
- Campaign Summary

Create a practical Growth Strategy.

IMPORTANT:

Return ONLY valid JSON.

Do NOT return markdown.

Keep every array to a maximum of 5 items.

Keep every description under 20 words.

Keep the roadmap to a maximum of 5 phases.

Keep the final summary under 150 words.

Return exactly this schema:

{
    "acquisition_channels": [],
    "activation_strategy": [],
    "retention_strategy": [],
    "referral_strategy": [],
    "revenue_growth": [],
    "growth_experiments": [],
    "north_star_metric": "",
    "kpis": [],
    "roadmap": [],
    "summary": ""
}
"""
