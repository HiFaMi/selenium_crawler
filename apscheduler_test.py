#!/usr/bin/env python
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

import time
from selenium_twitter import twitter_crawler


# test
def job():
    print("I'm working.... | [time] {}:{}:{}".format(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))


# download = twitter_crawler()


sched = BackgroundScheduler()
sched.start()

# sched.add_job(job, 'interval', seconds=3, id='test_1')
sched.add_job(twitter_crawler, 'cron',  hour=1, id='test_1', next_run_time=datetime.datetime.now())


f = open('crawler_date.txt', 'a')
f.write("Run crawler date = {}-{}\n".format(time.localtime().tm_mon, time.localtime().tm_yday))
f.write("Run crawler time = {}:{}:{}".format(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
