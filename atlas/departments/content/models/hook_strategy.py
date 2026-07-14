"""
Hook Strategy
"""

from dataclasses import dataclass


@dataclass
class HookStrategy:
    workspace_id: str

    opening_hooks: list

    curiosity_hooks: list

    emotional_hooks: list

    authority_hooks: list

    contrarian_hooks: list

    short_form_hooks: list

    long_form_hooks: list

    recommendations: list

    summary: str
