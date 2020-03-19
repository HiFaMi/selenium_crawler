#!/usr/bin/env python

import os
import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_crawling import twitter_login, save_and_load_cookie, download_twitter_image, download_twitter_image_to_s3, twitter_login_headless

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, ".secret")

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))

email = secrets["TWITTER_EMAIL"]
password = secrets["TWITTER_PASSWORD"]


def twitter_crawler():

    # twitter login
    driver = twitter_login_headless(email, password)

    driver.implicitly_wait(10)
    driver.maximize_window()

    search_box = driver.find_element_by_xpath(
        """//*[@id="react-root"]/div/div/div/main/div/div/div\
        /div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input"""
    )

    # 검색
    search_box.send_keys("#박보영")

    elements = driver.find_elements_by_css_selector(
        "div.css-1dbjc4n.r-1awozwy.r-1iusvr4.r-18u37iz.r-46vdb2.r-1wtj0ep.r-5f2r5o.r-bcqeeo > div > div.css-901oao.css-bfa6kz.r-1re7ezh.r-18u37iz.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > span"
    )

    top_three_list = []

    for i in range(3):
        element_list = elements[i].text.split('@')
        top_three_list.append(element_list[-1])

    for sns in top_three_list:
        change_url = "https://twitter.com/" + str(sns)
        print(change_url)
        # cookie save and load
        save_and_load_cookie(driver=driver, change_url=change_url)

        driver.refresh()
        change_to_media = driver.find_element_by_css_selector(
            "nav > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-tzz3ar.r-1pi2tsx.r-hbs49y > div:nth-child(3) > a")
        change_to_media.click()

    # wait = WebDriverWait(driver, 10)
    # find_imgs = wait.until(EC._find_elements(
    #     (By.CSS_SELECTOR, "div > img")))

        time.sleep(3)
        find_imgs = driver.find_elements_by_css_selector("div > img")
        download_twitter_image_to_s3(imgs_element=find_imgs, user_name=sns)

        # set loading time
        SCROLL_PAUSE_TIME = 4

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            find_imgs = driver.find_elements_by_css_selector("div > img")
            download_twitter_image_to_s3(imgs_element=find_imgs, user_name=sns)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("{} is done".format(sns))
                break
            last_height = new_height
    driver.quit()


if __name__ == '__main__':
    twitter_crawler()
