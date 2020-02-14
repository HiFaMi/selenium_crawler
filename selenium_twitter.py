import os
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium_crawling import twitter_login
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

wait = WebDriverWait(driver, 10)

# element = wait.until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR,
#      "div > div.css-1dbjc4n:nth-child(2) > div.r-my5ep6.r-rull8r.r-qklmqi.r-6dt33c.r-o7ynqc.r-1j63xyz.css-18t94o4.css-1dbjc4n")))

element = driver.find_element_by_css_selector(
    "div > div.css-1dbjc4n:nth-child(3) > div.r-my5ep6.r-rull8r.r-qklmqi.r-6dt33c.r-o7ynqc.r-1j63xyz.css-18t94o4.css-1dbjc4n > div"
)
print(element.text)
element_list = element.text.split('@')
change_url = "https://twitter.com/"+ str(element_list[-1])
driver.get(change_url)
