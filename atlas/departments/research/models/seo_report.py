"""
SEO Report
"""

from dataclasses import dataclass, field


@dataclass
class SEOReport:
    workspace_id: str

    primary_keywords: list = field(default_factory=list)

    long_tail_keywords: list = field(default_factory=list)

    high_intent_keywords: list = field(default_factory=list)

    content_clusters: list = field(default_factory=list)

    faq_questions: list = field(default_factory=list)

    featured_snippets: list = field(default_factory=list)

    internal_linking: list = field(default_factory=list)

    summary: str = ""
