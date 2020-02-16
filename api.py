import scrapy
from scrapy.crawler import CrawlerProcess
from finn_scraper.spiders.letting import LettingSpider

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})

TEST_URL = "https://www.finn.no/realestate/lettings/search.html?floor_navigator=NOTFIRST&geoLocationName=Kols%C3%A5s&lat=59.91364&lon=10.51192&radius=10000&sort=2"

process.crawl(
    LettingSpider,
    base=TEST_URL
    #floor_navigator="NOTFIRST",  # ikke første etasje
    #location=0.20061,  # Oslo
)

process.start()
