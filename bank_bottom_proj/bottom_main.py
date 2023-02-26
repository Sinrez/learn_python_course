# https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2
# https://www.banki.ru/services/responses/list/?page=2&is_countable=on&rate[]=1&rate[]=2
# source env_bottom/bin/activate

import requests as re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
fake_ua = {'user-agent': ua.random}
resp = re.get(url='https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2', headers=fake_ua)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)


#заготовка
def parser():
    url_base_1 = 'https://www.banki.ru'

if __name__ == '__main__':
    pass