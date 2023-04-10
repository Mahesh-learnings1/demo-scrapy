import scrapy
from..items import QuotesDemoItem

class Demo3Spider(scrapy.Spider):
    name = "demo3"
    start_urls = ["https://quotes.toscrape.com/page/1/"]
    base_url = "https://quotes.toscrape.com/"

    def parse(self, response):
        base_class = response.css('.quote')

        items = QuotesDemoItem()
        for base in base_class:
            quote = base.css('.text::text').extract()
            author = base.css('.author::text').extract()
            author_link = [self.base_url + link for link in base.css('span a::attr(href)').extract()]
            tag = base.css('.tag::text').extract()
            tag_link = [self.base_url + link for link in base.css('.tag::attr(href)').extract()]

            items['quote'] = quote
            items['author'] = author
            items['author_link'] = author_link
            items['tag'] = tag
            items['tag_link'] = tag_link

            yield items
