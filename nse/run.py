from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.companies_spider import CompaniesSpider


def crawl_nse_site():
    process = CrawlerProcess(get_project_settings())

    # 'followall' is the name of one of the spiders of the project.
    process.crawl('companies')
    process.start()  # the script will block here until the

    # # Set up crawler
    # crawler = Crawler(Settings({'FEED_FORMAT': 'jsonlines',
    #                             'FEED_URI': 'result.jl'}))
    # crawler.configure()
    # crawler.crawl(spider)
    # crawler.start()
    # log.start()
    # reactor.run()  # the script will block here

if __name__ == '__main__':
    crawl_nse_site()

