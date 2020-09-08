"""
Defines a company who operates in the short-term loan space
"""

from enum import Enum
from loans_db.models.store import Store
from typing import Set, Dict, Any


class CompanyType(Enum):
    """
    Defines the company's main line of business
    """
    BROKER = 1
    LENDER = 2

class Company:
    """
    Represents one company
    """
    def __init__(self):
        self._id: str = "" # Just using the company name for now
        self.locations: Set[Store] = set()
        self.allVirtual: bool = False
        self.url: str = ""
        self.apr: float = None
        self.aliases: Set[str] = set()
        self.groups: Set[str] = set()

    def add_location(self, location):
        location.company_id = self._id
        self.locations.add(location)

    def as_dict(self) -> Dict[str, Any]:
        return {
            '_id': self._id,
            'locations': [location._id for location in self.locations],
            'allVirtual': self.allVirtual,
            'url': self.url,
            'apr': self.apr,
            'groups': [group for group in self.groups],
            'aliases': [alias for alias in self.aliases]
        }