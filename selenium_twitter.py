import os
import json
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium_crawling import twitter_login, save_and_load_cookie
from selenium.webdriver.support import expected_conditions as EC

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, ".secret")

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))

email = secrets["TWITTER_EMAIL"]
password = secrets["TWITTER_PASSWORD"]

driver = twitter_login(email, password)


driver.implicitly_wait(10)
driver.maximize_window()

search_box = driver.find_element_by_xpath(
    """//*[@id="react-root"]/div/div/div/main/div/div/div\
    /div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input"""
)

search_box.send_keys("#박보영")

element = driver.find_element_by_css_selector(
    "div > div.css-1dbjc4n:nth-child(3) > div.r-my5ep6.r-rull8r.r-qklmqi.r-6dt33c.r-o7ynqc.r-1j63xyz.css-18t94o4.css-1dbjc4n > div"
)
print(element.text)
element_list = element.text.split('@')
change_url = "https://twitter.com/" + str(element_list[-1])

save_and_load_cookie(driver=driver, change_url=change_url)

driver.refresh()
# change_to_media = driver.find_element_by_css_selector(
#     "nav > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-tzz3ar.r-1pi2tsx.r-hbs49y > div:nth-child(3) > a")
# change_to_media.click()
