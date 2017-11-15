from scrapy.utils.project import get_project_settings
# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from spiders.companies_spider import CompaniesSpider

# from scrapy import log, signals
from scrapy.crawler import CrawlerProcess
# from scrapy.settings import Settings
# from scrapy.xlib.pydispatch import dispatcher


# def stop_reactor():
#     reactor.stop()


def crawl_nse_site():
    process = CrawlerProcess(get_project_settings())

    # 'companies' is the name of one of the spiders of the project.
    process.crawl('companies')
    process.start()  # the script will block here until the crawling is
    # finished

    # dispatcher.connect(stop_reactor, signal=signals.spider_closed)
    # spider = CompaniesSpider()
    #
    # crawler = Crawler(spider, Settings())
    # # crawler.configure()
    # crawler.crawl(spider)
    # # crawler.start()
    # # log.start()
    # log.msg('Running reactor...')
    # reactor.run()  # the script will block here until the spider is closed
    # log.msg('Reactor stopped.')

    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    # runner = CrawlerRunner(get_project_settings())
    # #
    # d = runner.crawl(CompaniesSpider)
    # d.addBoth(lambda _: reactor.stop())
    # reactor.run()
    # the script will block here until the crawling is finished

if __name__ == '__main__':
    crawl_nse_site()
