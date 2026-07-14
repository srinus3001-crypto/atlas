"""
Content Summary
"""

from dataclasses import dataclass


@dataclass
class ContentSummary:
    workspace_id: str

    executive_summary: str

    trend_summary: str

    audience_summary: str

    topic_summary: str

    hook_summary: str

    script_summary: str

    story_summary: str

    cta_summary: str

    strategic_recommendations: list

    publishing_checklist: list

    next_steps: list
