from crawlers.baseCrawler import BaseCrawler
from bs4 import BeautifulSoup
import requests
from loans_db.models.store import Store

URL = 'https://www.expresscheckadvance.com/locations/results/'
LA = 'LA/30.9842977/-91.96233269999999/' # Louisianna is pretty much central to their locations
MILES_FROM_CENTER = '4000' # They allow you to increase this number up to about 5000 before throwing a db error
PARSER = 'lxml'

class ECA(BaseCrawler):

    @staticmethod
    def _parse_hours(hours):
        pass

    @staticmethod
    def _parse_location(location):
        store = Store()
        store.hours = ECA._parse_hours(location.find('ul', attrs={'class': 'hourset'}))
        store.name = location.find('h2').text.strip()
        info = location.find('span').text.split('\n')
        info = list(map(lambda x: x.strip(), info))
        store.phone_number = info[4].strip()
        store.loacation_description = info[3].strip()
        store.add_addr(' '.join(info[0:3]))
        return store

    @staticmethod
    def crawl():
        all_locations = []
        resp = requests.get(URL + LA + MILES_FROM_CENTER)
        soup = BeautifulSoup(resp.text, PARSER)
        locations_list = soup.find('ul', attrs={'id': 'locations-list'})
        for location in locations_list.findAll('li', recursive=False):
            new_location = ECA._parse_location(location)
            all_locations.append(new_location)
        return all_locations