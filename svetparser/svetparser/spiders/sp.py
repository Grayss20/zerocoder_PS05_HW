import scrapy


class SpSpider(scrapy.Spider):
    name = "sp"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css("div.wYUX2")
        for svet in svets:
            yield {
                "name": svet.css("a span::text").get(),
                "price": svet.css("span.ui-LD-ZU.KIkOH::text").get(),
                "url": svet.css("a::attr(href)").get()  
            }
