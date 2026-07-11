"""
Business Goal
"""

from dataclasses import dataclass


@dataclass
class BusinessGoal:
    goal_id: str
    title: str
    objective: str
    priority: str
    target: str
