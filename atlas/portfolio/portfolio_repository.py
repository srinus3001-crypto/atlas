"""
Portfolio Repository
"""

import json

from pathlib import Path

from dataclasses import asdict


class PortfolioRepository:
    def __init__(self):
        self.root = Path("knowledge/portfolios")

        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, portfolio):
        folder = self.root / portfolio.portfolio_id

        folder.mkdir(parents=True, exist_ok=True)

        with open(folder / "portfolio.json", "w", encoding="utf-8") as f:
            json.dump(asdict(portfolio), f, indent=4, default=str)
