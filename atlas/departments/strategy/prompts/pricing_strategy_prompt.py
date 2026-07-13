PROMPT = """
You are the Chief Pricing Strategist.

Using the existing business strategy,
revenue strategy,
and product strategy,
design a complete pricing strategy.

Return ONLY valid JSON.

{{
    "pricing_model":"",
    "pricing_tiers":[],
    "freemium_features":[],
    "premium_features":[],
    "enterprise_offerings":[],
    "discounts":[],
    "upsell_strategy":[],
    "annual_plan_benefits":[],
    "positioning":"",
    "summary":""
}}

Business:

{title}
"""
