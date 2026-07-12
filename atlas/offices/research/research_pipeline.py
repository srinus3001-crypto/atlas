"""
Research Pipeline

Coordinates multiple research agents.
"""

from atlas.offices.research.agents.executive_summary_agent import ExecutiveSummaryAgent
from atlas.offices.research.agents.market_agent import MarketAgent
from atlas.offices.research.agents.audience_agent import AudienceAgent
from atlas.offices.research.agents.competitor_agent import CompetitorAgent
from atlas.offices.research.agents.opportunity_agent import OpportunityAgent
from atlas.offices.research.agents.risk_agent import RiskAgent


class ResearchPipeline:
    def execute(self, mission):
        return {
            "executive_summary": ExecutiveSummaryAgent().execute(mission),
            "market_size": MarketAgent().execute(mission),
            "audience_analysis": AudienceAgent().execute(mission),
            "competitor_analysis": CompetitorAgent().execute(mission),
            "top_opportunities": OpportunityAgent().execute(mission),
            "risks": RiskAgent().execute(mission),
        }
        
