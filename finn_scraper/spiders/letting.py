# -*- coding: utf-8 -*-
import scrapy


class LettingSpider(scrapy.Spider):
    name = 'letting'
    allowed_domains = ['finn.no']

    # Filter: Location=Oslo
    # start_urls = [
    #     'https://www.finn.no/realestate/lettings/search.html?location=0.20061&page=1',
    #     'https://www.finn.no/realestate/lettings/search.html?location=0.20061&page=2',
    #     'https://www.finn.no/realestate/lettings/search.html?location=0.20061&page=3'
    # ]

    def __init__(self, location=None, *args, **kwargs):
        super(LettingSpider, self).__init__(*args, **kwargs)
        # location=0.20061 (Oslo)
        self.start_urls = [
            'https://www.finn.no/realestate/lettings/search.html?location=%s' % location
        ]

    def parse(self, response):

        self.logger.info('A response from %s just arrived!', response.url)
        
        for ad in response.css('article.ads__unit'):

            yield {
                'type':      ad.css('div.ads__unit__content > div > div > div.ads__unit__content__list::text').getall(),
                'keys':      ad.css('div.ads__unit__content > div.ads__unit__content__keys > div::text').getall(),
                'details':   ad.css('div.ads__unit__content > div.ads__unit__content__details > div::text').get(),
                'sponsored': ad.css('div.ads__unit__content > * > div.status--sponsored::text').get(),
                'finnkode':  ad.css('div.ads__unit__content > h2 > a::attr(data-finnkode)').get(),
                'id':        ad.css('div.ads__unit__content > h2 > a::attr(id)').get(),
                'href':      ad.css('div.ads__unit__content > h2 > a::attr(href)').get(),
                'title':     ad.css('div.ads__unit__content > h2 > a::text').get().strip(),
                'img':       ad.css('div.ads__unit__img > div > img::attr(src)').get()
            }

        next_page = response.css("* > div > nav > a.button--icon-right::attr(href)").get()
        print("---------------------------------------------------------------")
        print(next_page)
        print("---------------------------------------------------------------")
        if next_page:
            #next_page = response.urljoin(next_page)
            next_page = "https://www.finn.no" + next_page
            yield scrapy.Request(next_page, callback=self.parse)
