import time

import scrapy

from items import NseItem


class CompaniesSpider(scrapy.Spider):
    name = "companies"

    def start_requests(self):
        urls = [
            'https://www.nse.co.ke/market-statistics.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        market_stats = response.xpath('//table/tbody/tr/td//text()').extract()
        market_stats = [stat.strip() for stat in market_stats]
        market_stats = list(filter(None, market_stats))

        companies = market_stats[::7]
        volume = market_stats[1::7]
        highs = market_stats[2::7]
        lows = market_stats[3::7]
        last_traded_prices = market_stats[4::7]
        previous_prices = market_stats[5::7]
        changes = market_stats[6::7]

        item = NseItem()
        for index, company in enumerate(companies):
            item = self.create_meta(item, [company, volume[index],
                                    highs[index], lows[index],
                                    last_traded_prices[index],
                                    previous_prices[index], changes[index]])
            yield item

    @staticmethod
    def create_meta(item, stock_data):
        """
        Add data to the item
        """
        item['name'] = stock_data[0]
        item['volume'] = stock_data[1]
        item['high'] = stock_data[2]
        item['low'] = stock_data[3]
        item['last_traded_price'] = stock_data[4]
        item['prev_price'] = stock_data[5]
        item['change'] = stock_data[6]
        item['date'] = time.strftime("%c")
        return item
