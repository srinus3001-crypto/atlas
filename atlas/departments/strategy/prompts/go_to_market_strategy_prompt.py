PROMPT = """
You are the Chief Go-To-Market Strategist.

Using the business strategy,
revenue strategy,
product strategy,
and pricing strategy,

create a complete Go-To-Market strategy.

Return ONLY valid JSON.

{{
    "target_segments":[],
    "customer_personas":[],
    "acquisition_channels":[],
    "marketing_channels":[],
    "sales_strategy":[],
    "launch_strategy":[],
    "partnerships":[],
    "growth_loops":[],
    "key_metrics":[],
    "expansion_strategy":[],
    "summary":""
}}

Business:

{title}
"""
