# https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2
# https://www.banki.ru/services/responses/list/?page=2&is_countable=on&rate[]=1&rate[]=2
# source env_bottom/bin/activate

import requests as re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import json


ua = UserAgent()
fake_ua = {'user-agent': ua.random}

url_in = 'https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2'
resp = re.get(url=url_in,  headers=fake_ua)
with open('res.txt','w') as fl:
    fl.write(resp.text)
# print(resp.text)

# soup = BeautifulSoup(resp)
# print(soup)


#заготовка
def parser():
    url_base_1 = 'https://www.banki.ru'

if __name__ == '__main__':
    pass