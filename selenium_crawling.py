from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def instagram_login():
    usr_email = "mgkim1994@naver.com"
    usr_password = "kpy680126"

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
