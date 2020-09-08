from crawlers.baseCrawler import BaseCrawler
from bs4 import BeautifulSoup
import requests
import json
from loans_db.models.store import Store

URL = 'https://www.acecashexpress.com/'
PARSER = 'lxml'


class AceCashExpress(BaseCrawler):

    @staticmethod
    def _parse_location(location):
        location = json.loads(location)
        store = Store()
        store.name = location['Url']
        store.addr_street = location['Address']
        store.addr_city = location['City']
        store.addr_state = location['State']
        store.addr_zip = location['ZipCode']
        store.lon = location['Coords']['Longitude']
        store.lat = location['Coords']['Latitude']
        store.phone_number = location['Phone']['Number']
        return store

    @staticmethod
    def _parse_city(city_page):
        # This parser extracts its data from the "Make this My Home Store" buttons
        buttons = city_page.findAll('button', attrs={'class': 'btn btn-link btn-set-store'})
        stores = []
        for button in buttons:
            store = AceCashExpress._parse_location(button.get('data-storeinfo'))
            stores.append(store)
        return stores

    @staticmethod
    def _parse_state(state_page):
        stores = []
        cities = state_page.find('ul', attrs={'class': 'cities-list'})
        for city in cities.findAll('a'):
            resp = requests.get(URL + city.get('href'))
            soup = BeautifulSoup(resp.text, PARSER)
            stores += AceCashExpress._parse_city(soup)
        return stores

    @staticmethod
    def crawl():
        stores = []
        home = requests.get(URL + 'locations')
        soup = BeautifulSoup(home.text, PARSER)
        states = soup.find('ul', attrs={'class': 'states'})

        for state in states.findAll('a'):
            resp = requests.get(URL + state.get('href'))
            soup = BeautifulSoup(resp.text, PARSER)
            stores += AceCashExpress._parse_state(soup)
        return stores
