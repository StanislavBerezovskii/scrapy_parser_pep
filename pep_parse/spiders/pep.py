import re
import scrapy

from urllib.parse import urljoin

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_REGEXP


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('section#numerical-index td a::attr(href)')
        for pep_obj in peps:
            pep_link = urljoin(
                'https://peps.python.org/',
                pep_obj.extract(), '/'
            )
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().replace('-', '')
        number, name = re.search(PEP_REGEXP, title).groups()
        status = (
            response.css('dt:contains("Status") + dd').css('abbr::text').get()
        )
        yield PepParseItem({
            'number': number,
            'name': name,
            'status': status,
        })
