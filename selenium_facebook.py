#!/usr/bin/env python

import os
import json
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_crawling import facebook_login, download_facebook_image, download_facebook_image_to_s3

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
    driver.find_element_by_css_selector("#js_c > form > button").click()

    driver.maximize_window()

    element = driver.find_element_by_css_selector(
        """#xt_uniq_2 > div._77we > div > div._6v_a > div._6v-_ > div._6v_0._4ik4._4ik5 > a"""
    )
    element.click()

    wait = WebDriverWait(driver, 10)
    move_picture_post = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, """#u_fetchstream_2_4 > div:nth-child(3) > a""")))
    move_picture_post.click()

    driver.find_element_by_xpath("""//*[@id="js_1z"]/div/div[2]/div[2]/div[1]/a[1]/div/div[1]""").click()
    driver.find_element_by_xpath("""//*[@id="2762459600649210"]/a/img""").click()

    count = 0
    while True:
        time.sleep(2)
        picture = driver.find_element_by_css_selector("div > div > img.spotlight")
        src = picture.get_attribute('src')

        download = download_facebook_image(src=src)

        if download is False:
            break

        count += 1
        driver.find_element_by_css_selector("a.next").click()

    print(f'{count} images downloaded')
    driver.quit()


def selenium_facebook_to_s3():
    driver = facebook_login(email=email, password=password)

    driver.implicitly_wait(10)

    try:
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("#박보영")
        driver.find_element_by_css_selector("#js_c > form > button").click()

        driver.maximize_window()

        element = driver.find_element_by_css_selector(
            """#xt_uniq_2 > div._77we > div > div._6v_a > div._6v-_ > div._6v_0._4ik4._4ik5 > a"""
        )
        element.click()

        wait = WebDriverWait(driver, 10)
        move_picture_post = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, """#u_fetchstream_2_4 > div:nth-child(3) > a""")))
        move_picture_post.click()

        driver.find_element_by_xpath("""//*[@id="js_1z"]/div/div[2]/div[2]/div[1]/a[1]/div/div[1]""").click()
        driver.find_element_by_xpath("""//*[@id="2762459600649210"]/a/img""").click()

        count = 0
        while True:
            time.sleep(2)
            picture = driver.find_element_by_css_selector("div > div > img.spotlight")
            src = picture.get_attribute('src')

            download = download_facebook_image_to_s3(src=src, aws_access_key=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

            if download is False:
                break

            count += 1
            driver.find_element_by_css_selector("a.next").click()

        print(f'{count} images downloaded')

    finally:
        driver.quit()


def run_selenium_facebook():
    while True:
        try:
            selenium_facebook_to_s3()
            break

        except:
            print('Try again...')


if __name__ == "__main__":
    selenium_facebook_to_s3()
