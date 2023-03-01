# https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2
# https://www.banki.ru/services/responses/list/?page=2&is_countable=on&rate[]=1&rate[]=2
# href="/services/responses/bank/response/
# source env_bottom/bin/activate

import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
import os


url_1 = 'https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2'
url_max = 'https://www.banki.ru/services/responses/list/?page=1440&is_countable=on&rate[]=1&rate[]=2' # c начала 2022.

url_from_parse = []

def urls_parser(url_in):
    url_base_1 = 'https://www.banki.ru'
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}

    resp = req.get(url=url_in,  headers=fake_ua)
    bs = BeautifulSoup(resp.text, 'lxml')
    bs_res_1 = bs.find_all('a', attrs={'class':"link-simple"})
    for b in bs_res_1:
        href = b.attrs.get("href")
        if '/services/responses/bank/response/' in href:
            url_from_parse.append(url_base_1+href)

def page_parser(url_page):
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}

    resp_fe = req.get(url=url_page,  headers=fake_ua)
    bs2 = BeautifulSoup(resp_fe.text, 'html.parser')

    #получаем краткий отзыв - название отзыва
    short_fee = bs2.find_all('h1', class_ = "text-header-0 le856f50c")
    short_feedback = str([s.get_text() for s in short_fee][0]).strip()
    #получаем название банка 
    bank_na = bs2.find('img', class_='lazy-load')
    bank_name = str(bank_na).split()[1].replace('alt="','').replace('"','')
    #получаем полный отзыв
    resp = bs2.find('div', class_='lb1789875 markdown-inside markdown-inside--list-type_circle-fill')
    response_full = [s.get_text() for s in resp]
    #получаем дату отзыва replace("['\n', ","").replace("'\n']","")
    dt = bs2.find('span', class_='l10fac986')
    response_date = [d.get_text().strip() for d in dt][0]
    #получаем город 
    ct = bs2.find('span', class_='l3a372298')
    response_city = [c.get_text().strip() for c in ct][0]
    #получаем id отзыва
    id_url = url_page.split('/')[7]
    # print(id_url)

    return id_url, url_page, bank_name, short_feedback, response_date, response_city, response_full


if __name__ == '__main__':
    # url_test = 'https://www.banki.ru/services/responses/bank/response/10847043/'
    urls_parser(url_1)
    for url in url_from_parse:
        print(page_parser(url))
    # print(page_parser(url_test))

