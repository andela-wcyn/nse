from run import crawl_nse_site


import schedule
import time

# Adjusting to UTC time on Heroku Server (3 hours behind)
schedule.every().day.at("05:15").do(crawl_nse_site)  # Every midday

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute
