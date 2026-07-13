"""
Go-To-Market Strategy
"""

from dataclasses import dataclass, field


@dataclass
class GoToMarketStrategy:
    workspace_id: str

    target_segments: list = field(default_factory=list)

    customer_personas: list = field(default_factory=list)

    acquisition_channels: list = field(default_factory=list)

    marketing_channels: list = field(default_factory=list)

    sales_strategy: list = field(default_factory=list)

    launch_strategy: list = field(default_factory=list)

    partnerships: list = field(default_factory=list)

    growth_loops: list = field(default_factory=list)

    key_metrics: list = field(default_factory=list)

    expansion_strategy: list = field(default_factory=list)

    summary: str = ""
