import scrapy


class Demo2Spider(scrapy.Spider):
    name = "demo2"
    start_urls = ["https://quotes.toscrape.com/page/1/"]
    base_url = "https://quotes.toscrape.com/"

    def parse(self, response):
        base_class = response.css('.quote')
        for base in base_class:
            quote = base.css('.text::text').extract()
            author = base.css('.author::text').extract()
            author_link = [self.base_url + link for link in base.css('span a::attr(href)').extract()]
            tag = base.css('.tag::text').extract()
            tag_link = [self.base_url + link for link in base.css('.tag::attr(href)').extract()]

            yield {
                'quote' : quote,
                'author': author,
                'author_link' : author_link,
                'tag' : tag,
                'tag_link' : tag_link
            }
