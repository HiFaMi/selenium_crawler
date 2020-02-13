import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_crawling import instagram_login


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, ".secret")

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))

email = secrets["INSTAGRAM_EMAIL"]
password = secrets["INSTAGRAM_PASSWORD"]
driver = instagram_login(email, password)

driver.implicitly_wait(10)
search_box = driver.find_element_by_css_selector(
    "div.LWmhU._0aCwM > input"
)
search_box.send_keys("박보영")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(
    (By.XPATH,
     """//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""")))

element.click()

