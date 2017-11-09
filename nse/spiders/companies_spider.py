import scrapy


class CompaniesSpider(scrapy.Spider):
    name = "companies"

    def start_requests(self):
        urls = [
            'https://www.nse.co.ke/market-statistics.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        delayed_feed = response.xpath('//div[@class="marquee"]/span/text()'
                                      ).extract()
        css_thing = response.css('div').extract()
        print('css thing:', css_thing)
        market_stats = response.xpath('//table/tbody/tr/td/text()').extract()
        filename = 'companies.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
