import pickle
import os.path
import ssl
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from urllib.parse import urlparse



def instagram_login(email, password):
    usr_email = email
    usr_password = password

    path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(10)
    driver.get("https://instagram.com")

    login_elem = driver.find_element_by_css_selector(
        "div.rgFsT > div:nth-child(2) > p > a"
         )

    login_elem.click()

    emei = driver.find_element_by_css_selector("div.-MzZI > div._9GP1n > label.f0n8F")
    emei.send_keys(usr_email)

    emei = driver.find_element_by_name("password")
    emei.send_keys(usr_password)
    emei.send_keys(Keys.RETURN)

    click_button = driver.find_element_by_css_selector("div.mt3GC > button.aOOlW.HoLwm")
    click_button.click()

    return driver


def twitter_login(email, password):

    path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path)
    driver.get("https://twitter.com")

    wait = WebDriverWait(driver, 10)

    login_elem = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         """//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div""")))
    login_elem.click()

    emei = wait.until(EC.element_to_be_clickable(
        (By.NAME, "session[username_or_email]")))
    emei.send_keys(email)

    emei = driver.find_element_by_name("session[password]")
    emei.send_keys(password)
    emei.submit()

    return driver


def save_and_load_cookie(driver, change_url):
    pickle.dump(driver.get_cookies(), open("login_live.pkl", "wb"))

    driver.get(change_url)
    for cookie in pickle.load(open("login_live.pkl", "rb")):
        if 'expiry' in cookie:
            del cookie['expiry']

        driver.add_cookie(cookie)


def download_twitter_image(imgs_element):
    ssl._create_default_https_context = ssl._create_unverified_context

    for find_img in imgs_element:
        src = find_img.get_attribute('src')
        url = urlparse(src)
        path_list = url.path.split("/")
        print(path_list)
        if path_list[1] == "media" and os.path.exists("img/" + path_list[2] + ".png") is False:
            urllib.request.urlretrieve(src, "img/" + path_list[2] + ".png")
