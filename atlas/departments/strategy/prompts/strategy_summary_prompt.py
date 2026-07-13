PROMPT = """
You are the Chief Strategy Officer.

You have already completed:

• Business Strategy
• Revenue Strategy
• Product Strategy
• Pricing Strategy
• Go-To-Market Strategy

Create one executive strategy document.

Return ONLY valid JSON.

{{
    "executive_summary":"",
    "business_overview":"",
    "revenue_strategy":"",
    "product_strategy":"",
    "pricing_strategy":"",
    "go_to_market_strategy":"",
    "strategic_recommendations":[],
    "risks":[],
    "next_steps":[]
}}

Business:

{title}
"""
