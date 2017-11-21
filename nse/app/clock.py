from run import crawl_nse_site

import schedule
import time

# Adjusting to UTC time on Heroku Server (3 hours behind)
schedule.every().day.at("15:00").do(crawl_nse_site)  # Every EOD at 1700 hrs
print "Starting clock..."
count = 0
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute
