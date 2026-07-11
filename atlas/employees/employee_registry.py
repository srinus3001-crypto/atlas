"""
Employee Registry

Atlas Enterprise Employees
"""

from atlas.employees.employee import Employee


class EmployeeRegistry:

    @staticmethod
    def research_director():

        return Employee(

            employee_id="EMP001",

            name="Atlas Research Director",

            title="Chief Research Officer",

            department="Research",

            reports_to="CEO",

            responsibilities=[

                "Market Research",

                "Competitor Analysis",

                "Audience Analysis",

                "Opportunity Identification"

            ],

            kpis=[

                "Research Accuracy",

                "Confidence Score",

                "Business Value"

            ],

            tools=[

                "Claude",

                "Mission Repository"

            ],

            ai_model="claude-sonnet-5",

            sop="Research SOP v1",

            authority="Approve Research"

        )

