import os
import json
import time

from selenium_crawling import twitter_login, save_and_load_cookie, download_twitter_image

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, ".secret")

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))

email = secrets["TWITTER_EMAIL"]
password = secrets["TWITTER_PASSWORD"]

# twitter login
driver = twitter_login(email, password)


driver.implicitly_wait(10)
driver.maximize_window()

search_box = driver.find_element_by_xpath(
    """//*[@id="react-root"]/div/div/div/main/div/div/div\
    /div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input"""
)

# 검색
search_box.send_keys("#박보영")

element = driver.find_element_by_css_selector(
    "div > div.css-1dbjc4n:nth-child(3) > div.r-my5ep6.r-rull8r.r-qklmqi.r-6dt33c.r-o7ynqc.r-1j63xyz.css-18t94o4.css-1dbjc4n > div"
)

element_list = element.text.split('@')
change_url = "https://twitter.com/" + str(element_list[-1])

# cookie save and load
save_and_load_cookie(driver=driver, change_url=change_url)

driver.refresh()
change_to_media = driver.find_element_by_css_selector(
    "nav > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-tzz3ar.r-1pi2tsx.r-hbs49y > div:nth-child(3) > a")
change_to_media.click()

time.sleep(2)
find_imgs = driver.find_elements_by_css_selector("div > img")
download_twitter_image(imgs_element=find_imgs)

# # set loading time
# SCROLL_PAUSE_TIME = 2
#
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     download_twitter_image(imgs_element=find_imgs)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
