from loans_db.crawlers.baseCrawler import BaseCrawler
from loans_db.models.company import Company
import json
from loans_db.db import get_db
from loans_db.crawlers.crawler_factory import factory

class FullCrawl(BaseCrawler):
    
    @staticmethod
    def _json_to_obj(json_dict):
        obj = Company()
        obj._id = json_dict['name']
        obj.url = json_dict.get('website', None)
        obj.aliases = set(json_dict.get('aliases'))
        obj.groups = set(json_dict.get('groups'))
        obj.apr = json_dict.get('apr')
        return obj

    @staticmethod
    def crawl():
        with open('hand_gathered.json') as in_file:
            companies = json.load(in_file)

        companies = list(map(FullCrawl._json_to_obj, companies))
        companies_dicts = []
        location_dicts = []
        for company in companies:
            # crawl and add locations
            if company._id in factory:
                locations = factory[company._id].crawl()
                for i, location in enumerate(locations):
                    company.add_location(locations[i])
                    locations[i]._id = location.generate_id()
                for location in set(locations):
                    location_dicts.append(location.as_dict())
            companies_dicts.append(company.as_dict())

        db = get_db()

        db.companies.insert(companies_dicts)
        db.locations.insert(location_dicts)

