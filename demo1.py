import scrapy


class Demo1Spider(scrapy.Spider):
    name = "demo1"
    start_urls = ["https://quotes.toscrape.com/page/1/"]
    base_url = "https://quotes.toscrape.com/"

    def parse(self, response):
        quote = response.css('.text::text').extract()
        author = response.css('.author::text').extract()
        author_source = [self.base_url + auth  for auth in response.css('.quote span a::attr(href)').extract()]
        tags = response.css('.tag::text').extract()
        tag_links = [self.base_url + link for link in response.css('.tag::attr(href)').extract()]

        yield {
            'quote' : quote,
            'author': author,
            'author_source' : author_source,
            'tags' : tags,
            'tag_links' : tag_links
        }
