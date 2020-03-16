#!/usr/bin/env python
import datetime
import sys

from apscheduler.schedulers.background import BackgroundScheduler

import time
from selenium_twitter import twitter_crawler


def job_crawler():
    while True:
        try:
            twitter_crawler()
            f = open('crawler_date.txt', 'a')
            f.write("Run crawler date = {}-{}\n".format(time.localtime().tm_mon, time.localtime().tm_yday))
            f.write("Run crawler time = {}:{}:{}".format(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))

            break

        except:
            print('try again......')
            print(sys.exc_info()[0])


if __name__ == '__main__':

    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(job_crawler, 'corn', day=15, hour=2, id='test_1', start_date=datetime.datetime.now())
    input("Press enter to exit.")
    sched.shutdown()
