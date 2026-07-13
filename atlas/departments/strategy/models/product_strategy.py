"""
Product Strategy
"""

from dataclasses import dataclass, field


@dataclass
class ProductStrategy:
    workspace_id: str

    core_product: str = ""

    product_features: list = field(default_factory=list)

    unique_selling_points: list = field(default_factory=list)

    customer_problems: list = field(default_factory=list)

    roadmap: list = field(default_factory=list)

    technology_stack: list = field(default_factory=list)

    competitive_positioning: str = ""

    scalability_plan: str = ""

    summary: str = ""
