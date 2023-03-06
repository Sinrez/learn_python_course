# source env_bottom/bin/activate

import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep
from random import randint
import os
from check_resource import check_url


categories = ['deposits','credits','creditcards','hypothec',
              'autocredits','remote','restructing','debitcards','transfers','other']
# limit = 150
# 1440 - c начала 22
limit = 2 # !!!cтавим на период теста чтобы не дудосить!!!
url_base_site = 'https://www.banki.ru'


def page_fliper(categor, limit):
    for cat in categor:
        #цикл перебора стартовой страницы форума для каждой категории
        url_categor_today=f'https://www.banki.ru/services/responses/list/product/{cat}/?is_countable=on&rate[]=1&rate[]=2'
        for url in urls_parser(url_categor_today,url_base_site):
            # print(url)
            #в этом месте добавить запись в бд
            # print(page_parser(url, cat))
            resp = page_parser(url, cat)
            with open('res.txt','a') as fl:
                    fl.write(str(resp))
                    fl.write('*'*30)

        # print('*'*30)
        sleep(randint(1,2))

    for cat in categor:
        #цикл перебора следуюших страниц, так как есть параметр page= и с ним не вытащить ссылки из цикла выше
        for l in range(1, limit+1):
            url_categor_history = f'https://www.banki.ru/services/responses/list/product/{cat}/?page={l}&is_countable=on&rate[]=1&rate[]=2'
            for url in urls_parser(url_categor_today,url_base_site):
                if url:
            # print(url)
            #в этом месте добавить запись в бд
                    # print(page_parser(url, cat))
                    # print('*'*30)
                    resp = page_parser(url, cat)
                    with open('res.txt','a') as fl:
                        fl.write(str(resp))
                        fl.write('*'*30)
            sleep(randint(1,2))

def urls_parser(url_in, url_base_site):
    url_from_parse = []
    try:
        check_url(url_in)
        ua = UserAgent()
        fake_ua = {'user-agent': ua.random}
        try:
            resp = req.get(url=url_in,  headers=fake_ua)
        except (req.RequestException, ValueError) as er_net:
            return f'Сетевая ошибка: {er_net}' 
        try:
            bs = BeautifulSoup(resp.text, 'lxml')
            bs_res_1 = bs.find_all('a', attrs={'class':"link-simple"})
        except AttributeError as ar0:
            return f'Произошла ошибка парсинга страниц отзыва: {ar0}'
        for b in bs_res_1:
            href = b.attrs.get("href")
            if '/services/responses/bank/response/' in href:
                url_from_parse.append(url_base_site+href)
        return url_from_parse
    except Exception as ex0:
        return f'Ошибка при переборе страниц: {ex0}'


def page_parser(url_page, category=''):
    try:
        check_url(url_page)
        ua = UserAgent()
        fake_ua = {'user-agent': ua.random}
        try:
            resp_fe = req.get(url=url_page,  headers=fake_ua)
            resp_fe.raise_for_status()
        except (req.RequestException, ValueError) as er_net:
            return f'Сетевая ошибка: {er_net}' 

        try:
            bs2 = BeautifulSoup(resp_fe.text, 'html.parser')
            #получаем краткий отзыв - название отзыва
            short_feedback = bs2.find('h1', class_ = "text-header-0 le856f50c").text.strip()
            #получаем название банка 
            bank_na = bs2.find('img', class_='lazy-load')
            bank_name = str(bank_na).split()[1].replace('alt="','').replace('"','')
            #получаем полный отзыв
            response_full = bs2.find('div', class_='lb1789875 markdown-inside markdown-inside--list-type_circle-fill').text.strip()
            #получаем дату отзыва
            response_date = bs2.find('span', class_='l10fac986').text.strip()
            #получаем город 
            response_city = bs2.find('span', class_='l3a372298').text
            #получаем id отзыва
            id_url = url_page.split('/')[7]
        except AttributeError as ar:
            return f'Произошла ошибка в блоке BeautifulSoup парсинга: {ar}'
        return id_url, url_page, bank_name, category, short_feedback, response_date, response_city, response_full
    except Exception as ex:
        return f'Произошла ошибка в функции page_parser: {ex}'
  
  
if __name__ == '__main__':
    page_fliper(categories, limit)

