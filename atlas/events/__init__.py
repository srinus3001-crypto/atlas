"""
Atlas Event System

Automatically registers all enterprise event listeners.
"""

from atlas.events.listeners.research_listener import listener

__all__ = [
    "listener"
]
