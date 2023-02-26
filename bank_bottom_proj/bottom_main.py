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
from requests_html import HTMLSession
import json


# session = HTMLSession()
# r = session.get('https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2')
# r.html.render()  
# print(r.html.text)


#selenium
op = webdriver.ChromeOptions()
# op.add_argument('headless')
op.add_argument("--start-maximized")
op.add_argument('--log-level=3')
driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),options=op)
driver.set_window_size(1920,1080)
url='https://www.banki.ru/services/responses/list/?page=2&is_countable=on&rate[]=1&rate[]=2'
driver.get(url)
sleep(400)
soup = BeautifulSoup(driver.page_source)
# values = soup.find_all(class_='a2m0z y2m0z H2m0z eG2mw SG2mw')
# driver.close()
print(soup)
driver.quit()
print("Done")

# req
# ua = UserAgent()
# fake_ua = {'user-agent': ua.random}
# resp = re.get(url='https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2', headers=fake_ua).text
# soup = BeautifulSoup(resp, 'html.parser').contents
# r_neg = requests.get('https://www.banki.ru/services/responses/list/?rate=1&is_countable=on&isMobile=0&page=1', headers=headers)
# laptop_soup_neg = BS(r_neg.content, 'html.parser')


#заготовка
def parser():
    url_base_1 = 'https://www.banki.ru'

if __name__ == '__main__':
    pass