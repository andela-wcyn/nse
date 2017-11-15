import logging
import sys

from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue

from nse.app.worker import conn
from nse.app.run import crawl_nse_site

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
scheduler = BlockingScheduler()
q = Queue(connection=conn)


def crawl_nse():
    q.enqueue(crawl_nse_site())


scheduler.add_job(crawl_nse)  # enqueue right away once
scheduler.add_job(crawl_nse, 'interval', minutes=1)
scheduler.start()
