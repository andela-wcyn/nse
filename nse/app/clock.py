from run import crawl_nse_site


import schedule
import time

# Adjusting to UTC time on Heroku Server (3 hours behind)
schedule.every().day.at("09:00").do(crawl_nse_site)  # Every midday
# schedule.every().day.at("14:00").do(crawl_nse_site)

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute
