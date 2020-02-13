import os
import json
from selenium_crawling import twitter_login

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, ".secret")

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))

email = secrets["TWITTER_EMAIL"]
password = secrets["TWITTER_PASSWORD"]

driver = twitter_login(email, password)


