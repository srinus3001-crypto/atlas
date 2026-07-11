"""
Office Registry

Registers all Atlas departments.
"""

from atlas.offices.research_office import ResearchOffice
from atlas.offices.content_office import ContentOffice


class OfficeRegistry:

    def __init__(self):

        self.offices = {

            "Research": ResearchOffice(),

            "Content": ContentOffice(),

        }

    def register(self, name, office):

        self.offices[name] = office

    def get(self, office_name):

        return self.offices.get(office_name)

