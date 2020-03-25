#!/usr/bin/env python

import os
import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_crawling import facebook_login

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, ".secret")

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))


email = secrets["SOCIAL"]["FACEBOOK_EMAIL"]
password = secrets["SOCIAL"]["FACEBOOK_PASSWORD"]

AWS_ACCESS_KEY = secrets['AWS']['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = secrets['AWS']['AWS_SECRET_ACCESS_KEY']


def selenium_facebook():
    driver = facebook_login(email=email, password=password)

    driver.implicitly_wait(10)


    search_box = driver.find_element_by_name("q")
    search_box.send_keys("#박보영")
    driver.implicitly_wait(10)
    search_box.submit()



    element = driver.find_element_by_xpath(
        """//*[@id="xt_uniq_2"]/div[1]/div/div[1]/div[1]/div[1]/a"""
    )
    element.click()

    wait = WebDriverWait(driver, 10)
    move_picture_post = wait.until(EC.element_to_be_clickable(
        (By.XPATH, """//*[@id="u_fetchstream_1_4"]/div[3]/a""")))
    move_picture_post.click()








if __name__ == "__main__":
    selenium_facebook()
