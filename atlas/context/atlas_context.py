"""
Atlas Context

Shared enterprise context passed between offices.
"""

from dataclasses import dataclass
from typing import Optional

from atlas.models.business_goal import BusinessGoal
from atlas.models.mission import Mission
from atlas.models.research_report import ResearchReport
from atlas.models.content_package import ContentPackage


@dataclass
class AtlasContext:

    business_goal: Optional[BusinessGoal] = None

    mission: Optional[Mission] = None

    research_report: Optional[ResearchReport] = None

    content_package: Optional[ContentPackage] = None

