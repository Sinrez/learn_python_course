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

# ua = UserAgent()
# fake_ua = {'user-agent': ua.random}
# resp = re.get(url='https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2', headers=fake_ua)
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),options=op)
url='https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2'
driver.get(url)
sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# values = soup.find_all(class_='a2m0z y2m0z H2m0z eG2mw SG2mw')
driver.close()
print(soup)


#заготовка
def parser():
    url_base_1 = 'https://www.banki.ru'

if __name__ == '__main__':
    pass