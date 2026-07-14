"""
Script Strategy
"""

from dataclasses import dataclass


@dataclass
class ScriptStrategy:
    workspace_id: str

    youtube_script: str

    linkedin_post: str

    x_thread: list

    newsletter: str

    blog_outline: list

    call_to_action: str

    keywords: list

    summary: str
