from atlas.departments.content.employees.chief_content_officer import (
    ChiefContentOfficer,
)


def main():
    plan = ChiefContentOfficer().create_plan()

    print(plan)


if __name__ == "__main__":
    main()
