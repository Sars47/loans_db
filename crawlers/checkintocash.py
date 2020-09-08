from loans_db.utils.crawler_utils import STATES
from crawlers.baseCrawler import BaseCrawler
import requests
from loans_db.models.store import Store

URL = 'https://local.checkintocash.com/'
DATA = {"postType": "location", "postsPerPage": -1}


class CheckIntoCash(BaseCrawler):

    @staticmethod
    def _parse_location(location):
        store = Store()
        store.phone_number = location['loc']['phone']
        store.name = location['key']
        store.addr_street = location['loc']['address1'] + location['loc']['address2']
        store.addr_city = location['loc']['city']
        store.addr_state = location['loc']['state']
        store.addr_zip = location['loc']['corporateCode']
        store.lon = location['loc']['longitude']
        store.lat = location['loc']['latitude']
        store.phone_number = location['loc']['phone']
        return store

    @staticmethod
    def crawl():
        stores = []
        for state in STATES:
            req = requests.get(URL + state.lower() + '.json')
            if req.status_code != 200:
                continue
            locations = req.json()
            for location in locations['keys']:
                store = CheckIntoCash._parse_location(location)
                stores.append(store)
        return stores
