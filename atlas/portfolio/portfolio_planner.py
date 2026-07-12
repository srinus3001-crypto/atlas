"""
Portfolio Planner
"""

from atlas.portfolio.content_portfolio import ContentPortfolio
from atlas.portfolio.portfolio_repository import PortfolioRepository


class PortfolioPlanner:
    def create(self, opportunity, decision):
        portfolio = ContentPortfolio(
            portfolio_id=f"P{opportunity.opportunity_id[1:]}",
            opportunity_title=opportunity.title,
            niche=opportunity.niche,
            source=opportunity.source,
            priority=decision.priority,
            score=opportunity.overall_score,
        )

        PortfolioRepository().save(portfolio)

        return portfolio
