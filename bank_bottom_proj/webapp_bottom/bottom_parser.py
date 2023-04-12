# source env_bottom/bin/activate
import sys

#это локальные костыли для доступности вспомогательных файлов, добавлять перед импортом основных библиотек
sys.path.append('..') 
sys.path.append('/Volumes/D/learn_python_course/bank_bottom_proj/webapp_bottom') 

from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import datetime
from utils import get_url, save_response
from config import categories
from check_resource import check_url

def page_fliper(categories: list = categories, start: int = 1, limit: int = 4) -> None:
    # limit = 150
    #1440 - c начала 22
    # limit = 4 # !!!cтавим на период теста чтобы не дудосить!!!
    url_base_site = 'https://www.banki.ru'
    check_url(url_base_site)
    for cat in categories:
        print(f'Обрабатываю категорию {cat}')
        print()
        #цикл перебора следуюших страниц, так как есть параметр page= и с ним не вытащить ссылки из цикла выше
        for l in range(start, limit+1):
            url_categor_history = f'https://www.banki.ru/services/responses/list/product/{cat}/?page={l}&is_countable=on&rate[]=1&rate[]=2'
            print(url_categor_history)
            for url in urls_parser(url_categor_history,url_base_site):
                if url:
                    # print(url)
                    try:
                        *result, = page_parser(url, cat)
                        save_response(*result)
                    except TypeError as te:
                        print(''.join(result))
                        print(f'Ошибка: {te}')
                        exit()
            sleep(randint(1,2))
            
def urls_parser(url_in: str, url_base_site: str) -> list:
    url_from_parse = []
    resp = get_url(url_in)
    try:
        bs = BeautifulSoup(resp.text, 'lxml')
        bs_res_1 = bs.find_all('a', attrs={'class':"link-simple"})
        for b in bs_res_1:
            href = b.attrs.get("href")
            if '/services/responses/bank/response/' in href:
                url_from_parse.append(url_base_site+href)
        return url_from_parse
    except AttributeError as ar0:
        return f'Произошла ошибка парсинга страниц отзыва: {ar0}'
    except Exception as ex0:
        return f'Ошибка при переборе страниц: {ex0}'

def page_parser(url_page: str, category: str ='') -> tuple:
        try:
            resp_fe = get_url(url_page)
            bs2 = BeautifulSoup(resp_fe.text, 'html.parser')
            #получаем краткий отзыв - название отзыва
            short_feedback = bs2.find('h1', class_ = "text-header-0 le856f50c").text.strip()
            #получаем название банка 
            bank_na = bs2.find('img', class_='lazy-load')
            bank_name = str(bank_na).split('"')[1].replace('alt="','').replace('"','')
            #на этом шаге название банка может отстустовать как alt текст картинки логотипа, тогда парсится Банки.ру, поэтому:
            if bank_name == 'Банки.ру':
                bank_na = bs2.find('span', class_='link-simple link-simple--theme_major-gray').text.strip()
                bank_name = bank_na
            #получаем полный отзыв
            response_full = bs2.find('div', class_='lb1789875 markdown-inside markdown-inside--list-type_circle-fill').text.strip()
            #получаем дату отзыва
            response_dt = bs2.find('span', class_='l10fac986').text.strip()
            response_date = datetime.strptime(response_dt, '%d.%m.%Y %H:%M')
            #получаем город 
            response_city = bs2.find('span', class_='l3a372298').text
            #получаем id отзыва
            id_url = url_page.split('/')[7]
        except AttributeError as ar:
            return f'Произошла ошибка в блоке BeautifulSoup парсинга: {ar}'
        except Exception as ex:
            return f'Произошла ошибка в функции page_parser: {ex}'
        return id_url, url_page, bank_name, category, short_feedback, response_date, response_city, response_full
    

if __name__ == '__main__':
    page_fliper()

    

