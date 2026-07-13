"""
SEO Strategy
"""

from dataclasses import dataclass


@dataclass
class SEOStrategy:
    workspace_id: str

    primary_keywords: list

    secondary_keywords: list

    content_clusters: list

    on_page_strategy: list

    technical_seo: list

    link_building_strategy: list

    local_seo: list

    measurement_metrics: list

    roadmap: list

    summary: str
