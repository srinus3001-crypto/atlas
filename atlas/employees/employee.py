"""
Atlas Employee
"""

from dataclasses import dataclass, field


@dataclass
class Employee:

    employee_id: str

    name: str

    title: str

    department: str

    reports_to: str

    responsibilities: list = field(default_factory=list)

    kpis: list = field(default_factory=list)

    tools: list = field(default_factory=list)

    ai_model: str = ""

    sop: str = ""

    authority: str = ""

    status: str = "ACTIVE"

