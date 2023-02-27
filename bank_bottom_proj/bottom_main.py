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


session = HTMLSession()
r = session.get('https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2')
r.html.render()  
# print(type(r.html.text))
# } } } ] } { "@context"
# print(r.html.text)
res = r.html.text
i1 = res.find('"review": [ {') + 10
i2 = res.rfind('} } } ] }') + 7
# print(res)
print(res[i1:i2])
# print(res)
# soup = BeautifulSoup(res).find_all_next('review')
# print(soup)


# # #selenium
# op = webdriver.ChromeOptions()
# # op.add_argument('headless')
# op.add_argument("--start-maximized")
# op.add_argument('--log-level=3')
# driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),options=op)
# driver.set_window_size(1920,1080)
# url='https://www.banki.ru/services/responses/list/?page=2&is_countable=on&rate[]=1&rate[]=2'

# print(p_element.text)
# sleep(400)
# soup = BeautifulSoup(driver.page_source)
# # values = soup.find_all(class_='a2m0z y2m0z H2m0z eG2mw SG2mw')
# # driver.close()
# print(soup)
# driver.quit()
# print("Done")

# req
# ua = UserAgent()
# fake_ua = {'user-agent': ua.random}
# resp = re.get(url='https://www.banki.ru/services/responses/list/?page=4&is_countable=on&rate[]=1&rate[]=2/application/ld+json', headers=fake_ua).text

# soup = BeautifulSoup(resp, 'html.parser').contents
# print(soup)


#заготовка
def parser():
    url_base_1 = 'https://www.banki.ru'

if __name__ == '__main__':
    pass