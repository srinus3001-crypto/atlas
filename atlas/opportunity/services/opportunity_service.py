"""
Opportunity Service
"""

# Initialize event listeners
import atlas.events

from atlas.opportunity.collectors.trend_collector import TrendCollector
from atlas.opportunity.scorers.opportunity_scorer import OpportunityScorer
from atlas.opportunity.repository.opportunity_repository import OpportunityRepository
from atlas.opportunity.judges.opportunity_judge import OpportunityJudge

from atlas.portfolio.portfolio_planner import PortfolioPlanner
from atlas.workspace.workspace_manager import WorkspaceManager


class OpportunityService:
    def discover(self):
        collector = TrendCollector()

        scorer = OpportunityScorer()

        repository = OpportunityRepository()

        judge = OpportunityJudge()

        planner = PortfolioPlanner()

        workspace_manager = WorkspaceManager()

        workspaces = []

        for opportunity in collector.collect():
            opportunity = scorer.score(opportunity)

            repository.save(opportunity)

            decision = judge.evaluate(opportunity)

            if not decision.approved:
                continue

            portfolio = planner.create(opportunity, decision)

            workspace = workspace_manager.create(portfolio)

            workspaces.append(workspace)

        return workspaces
