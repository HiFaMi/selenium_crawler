import pickle
import os.path
import ssl
import urllib.request
import boto3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from urllib.parse import urlparse
from botocore.errorfactory import ClientError


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


def twitter_login_headless(email, password):
    path = "/usr/local/bin/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(path, options=chrome_options)

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


def facebook_login(email, password):
    path = "/usr/local/bin/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(path, options=chrome_options)

    driver.get("https://facebook.com")

    driver.implicitly_wait(10)

    emei = driver.find_element_by_name("email")
    emei.send_keys(email)
    emei = driver.find_element_by_name("pass")
    emei.send_keys(password)
    emei.send_keys(Keys.ENTER)

    return driver


def save_and_load_cookie(driver, change_url):
    pickle.dump(driver.get_cookies(), open("login_live.pkl", "wb"))

    driver.get(change_url)
    for cookie in pickle.load(open("login_live.pkl", "rb")):
        if 'expiry' in cookie:
            del cookie['expiry']

        driver.add_cookie(cookie)


def download_twitter_image(imgs_element, user_name):
    ssl._create_default_https_context = ssl._create_unverified_context

    for find_img in imgs_element:
        src = find_img.get_attribute('src')
        url = urlparse(src)
        path_list = url.path.split("/")
        dir_path = 'app/.media/img/{}/'.format(user_name)

        if os.path.exists(dir_path) is False:
            os.mkdir(dir_path)

        if path_list[1] == "media" and os.path.exists(dir_path + path_list[2] + ".png") is False:
            urllib.request.urlretrieve(src, dir_path + path_list[2] + ".png")


def download_twitter_image_to_s3(imgs_element, user_name, aws_access_key, aws_secret_access_key):
    ssl._create_default_https_context = ssl._create_unverified_context

    session = boto3.Session(aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)
    s3_client = session.client('s3')
    bucket = 'selenium-crawler'

    for find_img in imgs_element:
        src = find_img.get_attribute('src')
        url = urlparse(src)
        path_list = url.path.split("/")
        dir_path = 'app/.media/img/'

        try:
            s3_client.head_object(Bucket=bucket, Key=f'.media/img/{user_name}')
        except ClientError:
            s3_client.put_object(Bucket=bucket, Key=f'.media/img/{user_name}/')

        if path_list[1] == "media":
            try:
                s3_client.head_object(Bucket=bucket, Key=f'.media/img/{user_name}/{path_list[2]}.png')

            except ClientError:
                urllib.request.urlretrieve(src, dir_path+path_list[2] + ".png")
                data = open(f'{dir_path}/{path_list[2]}.png', 'rb')
                s3_client.put_object(Bucket=bucket, Body=data, Key=f'.media/img/{user_name}/{path_list[2]}.png', ACL='public-read')
                os.remove(f'{dir_path}/{path_list[2]}.png')


def download_facebook_image(src):
    ssl._create_default_https_context = ssl._create_unverified_context

    url = urlparse(src)

    name = url.path.split('/')[-1][:-4]
    dir_path = 'app/.media/img/facebook/'

    if os.path.exists(dir_path + name + ".png") is False:
        urllib.request.urlretrieve(src, dir_path + name + ".png")

    else:
        return False
