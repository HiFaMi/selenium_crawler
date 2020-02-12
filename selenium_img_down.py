

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_crawling import instagram_login

driver = instagram_login()

driver.implicitly_wait(10)
search_box = driver.find_element_by_css_selector(
    "div.LWmhU._0aCwM > input"
)
search_box.send_keys("박보영")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(
    (By.XPATH,
     """//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""")))

# search_box.send_keys(Keys.RETURN)
element.click()

