import requests
from fake_useragent import UserAgent
from selenium import webdriver
from pgsql import *

DEBUG = True
ua = UserAgent(verify_ssl=False, cache=False)
base_url = 'https://'
url = f'{base_url}custom'


def get_html(url_link):
    headers = {'User-Agent': ua.random}
    r = requests.get(url_link, headers=headers).text
    return r


def get_html_over_selenium(url_link):
    driver = webdriver.Firefox()
    driver.get(url_link)
    html_page = driver.page_source
    driver.close()
    return html_page


def drop_and_create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def main():
    pass

if __name__ == '__main__':
    main()
