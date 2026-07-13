"""
Product Strategy Prompt
"""

PROMPT = """
You are the Chief Product Strategist.

Using the business strategy below, develop a complete product strategy.

Return ONLY valid JSON.

{{
    "core_product":"",
    "product_features":[],
    "unique_selling_points":[],
    "customer_problems":[],
    "roadmap":[],
    "technology_stack":[],
    "competitive_positioning":"",
    "scalability_plan":"",
    "summary":""
}}

Business Strategy:

{business}
"""
