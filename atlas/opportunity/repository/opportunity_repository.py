"""
Opportunity Repository
"""

import json

from pathlib import Path

from dataclasses import asdict


class OpportunityRepository:
    def __init__(self):
        self.root = Path("knowledge/opportunities")

        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, opportunity):
        folder = self.root / opportunity.opportunity_id

        folder.mkdir(parents=True, exist_ok=True)

        with open(folder / "opportunity.json", "w", encoding="utf-8") as f:
            json.dump(asdict(opportunity), f, indent=4, default=str)
