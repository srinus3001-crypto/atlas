"""
Research Department Test
"""

import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from atlas.departments.research.department import ResearchDepartment


def main():
    department = ResearchDepartment()

    department.execute(workspace_id="P001", title="AI replaces Software Engineers?")

    print()

    print("Research Department Test Completed")


if __name__ == "__main__":
    main()
