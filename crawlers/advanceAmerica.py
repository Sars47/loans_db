from crawlers.baseCrawler import BaseCrawler
import requests
from loans_db.models.store import Store

URL = 'https://www.advanceamerica.net/api/posts/filter'
REFERER = 'https://www.advanceamerica.net/store-locations'
DATA = {"postType": "location", "postsPerPage": -1}

class AdvanceAmerica(BaseCrawler):

    @staticmethod
    def _parse_location(location):
        store = Store()
        store.phone_number = location['fields']['phone']
        store.name = location['slug']
        store.addr_street = location['fields']['address']
        store.addr_city = location['fields']['city']
        store.addr_state = location['fields']['state']
        store.addr_zip = location['fields']['zip']
        store.lon = location['fields']['longitude']
        store.lat = location['fields']['latitude']
        return store

    @staticmethod
    def crawl():
        req = requests.post(URL, headers={'referer': REFERER}, data=DATA)
        locations = req.json()
        stores = []
        for location in locations['posts']:
            store = AdvanceAmerica._parse_location(location)
            stores.append(store)
        return stores
