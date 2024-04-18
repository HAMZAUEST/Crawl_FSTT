import scrapy

class FSTTSpider(scrapy.Spider):
    name = 'fstt_spider'
    start_urls = ['https://fstt.ac.ma/Portail2023/']

    def parse(self, response):
        links = response.css('div.swiper-slide a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_link)


    def parse_link(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        Content = response.css('div.elementor-element-faf7450 div.elementor-widget-container ::text').extract()
        Content = ' '.join(Content).strip()
        print("Title:", title)
        print('Content:', Content)

