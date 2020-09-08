from typing import Any, Dict


class Store:
    
    def __init__(self):
        self._id = None
        self.name: str = None
        self.company_id: str = None
        self.addr_street: str = None
        self.addr_city: str = None
        self.addr_state: str = None
        self.addr_zip: str = None
        self.loacation_description: str = None
        self.phone_number: str = None
        self.hours: Dict[str: str] = None
        self.lat: float = None
        self.lon: float = None

    def as_dict(self) -> Dict[str, Any]:
        return {
          '_id': self._id,
          'name': self.name,
          'company_id': self.company_id,
          'addr_street': self.addr_street,
          'addr_city': self.addr_city,
          'addr_state': self.addr_state,
          'addr_zip': self.addr_zip,
          'location_description': self.loacation_description,
          'phone_number': self.phone_number,
          'hours': self.hours,
          'latitude': self.lat,
          'longitude': self.lon
        }

    def add_addr(self, addr: str):
        self.addr_street 
        addr = addr.strip().split()
        self.addr_zip = addr[-1]
        self.addr_state = addr[-2]
        self.addr_street = ' '.join(addr[0:-2])

    def generate_id(self) -> str:
        return self.company_id + self.addr_street

    def __hash__(self):
        return hash(self._id)
    
    def __eq__(self, other):
        if isinstance(other, Store):
            return self._id == other._id
        return NotImplemented
