import scrapy

class BenchmarkSpider(scrapy.Spider):
    name = "benchmark"
    
    def __init__(self, selector=None, *args, **kwargs):
        super(BenchmarkSpider, self).__init__(*args, **kwargs)
        self.selector = selector
        with open('urls.txt', 'r') as f:
            self.start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        if self.selector:
            for item in response.css(self.selector):
                yield {'element': item.css('::text').get()}
        else:
            for href in response.css('a::attr(href)').getall():
                yield {'link': href}
