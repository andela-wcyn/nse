from run import crawl_nse_site


import schedule
import time

# Adjusting to UTC time on Heroku Server (3 hours behind)
schedule.every().day.at("21:25").do(crawl_nse_site)  # Every midday
print "Starting clock..."
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute
