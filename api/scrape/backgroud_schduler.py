from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
from api.scrape.scrape import ScrapeCryptoCurrency
import requests 




def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ScrapeCryptoCurrency, 'interval', minutes=3, args=[requests])
    scheduler.start()