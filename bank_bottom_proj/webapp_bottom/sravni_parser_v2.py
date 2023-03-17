# source env_bottom/bin/activate

from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import datetime
from utils import get_url, save_response
import re
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
from config import sravni_categories
from check_resource import check_url

def url_parser(url_in, url_base_site):
    # AttributeError - сайт через раз кидает 403
    try:
        res_url = []
        resp = get_url(url_in)
        try:
            bs2 = BeautifulSoup(resp.text, 'html.parser')
        except AttributeError as ar0:
            return f'Ошибка {ar0}, когда {resp.text}'
        for a in bs2.find_all('a', href=True):
                # href=True в данном случае вытащить вообще все ссылки
                matchh = re.search(r"^(/bank/)[a-z]*/otzyvy/[0-9]*/", a['href'])
                if matchh is not None and matchh not in res_url:
                    res_url.append(url_base_site+matchh[0])
        return set(res_url) # для исключения дублей
    except Exception as ex2:
         return f'Ошибка в модуде отбора ссылок отзывов {ex2}'

def page_parser(url_page: str, categor: str =''):
    try:
        # AttributeError - хитрожопыйсайт через раз кидает 403 или не возвращает ответ, запустить еще раз
        resp = get_url(url_page)
        try:
            bs2 = BeautifulSoup(resp.text, 'html.parser')
        except AttributeError as ar1:
            return f'Ошибка {ar1}, когда {resp.text}'        
        #получаем краткий отзыв - название отзыва
        try:
            sh = bs2.find('div', class_ = "review-card_title__zYdxx articleTypography_article-h3__wuxLw")
            short_feedback = sh.text.strip()
        except AttributeError as ar2:
            return f'Ошибка {ar2}, когда {sh}' 
        # получаем категорию на рус > берем класс на уровень выше
        # categ_rus = bs2.find('div', class_ ='_1n8o0h2 _vea58f _52n9a4').text.strip()
        # #получаем название банка 
        bank_name = bs2.find('div', class_ ='review-card_organization__leFN5 _1n8o0h2 _vea58f _1ivat6c _52n9a4').text.strip()
        # #получаем полный отзыв
        response_full = bs2.find('div', class_ ='review-card_text__jTUSq articleTypography_article-comment__Px4n0').text.strip()
        # #получаем дату отзыва
        try:
            response_dt = bs2.find('div', class_ ='_1n8o0h2 _vea58f _pbfp49').find('div',class_='h-color-D30 _1h41p0x').text.strip()
            response_date = datetime.strptime(response_dt, '%d %B %Y')
        except ValueError as ve:
            current_year = str(datetime.now().year)
            response_dt_in = response_dt+' '+current_year
            response_date = datetime.strptime(response_dt_in, '%d %B %Y')
        # #получаем город  
        response_city = bs2.find('div', class_ ='h-color-D30 h-ml-8 _1h41p0x _1gpt55s').text.strip()
        # #получаем id отзыва - 00 чтобы исключить совпадений с id отзывов из других ресурсов
        id_url = '00'+url_page.split('/')[6]
        #преобразум категории для совместимости с категориями продуктов из других ресурсов
        categor_format = categor.lower().replace('savings', 'deposits').replace('mortgage','hypothec')
    except Exception as ex3:
        return f'Ошибка в модуде парсинга страницы {ex3}'
    return id_url, url_page, bank_name, categor_format, short_feedback, response_date, response_city, response_full
    

def page_fliper(categor):
        res_url = {}
        url_base_site = 'https://www.sravni.ru'
        check_url(url_base_site)
        for cat in categor:
            url_base = f'https://www.sravni.ru/banki/otzyvy/?tag={cat}&rated=one&rated=two&rated=three'
            url_from_parse = (url_parser(url_base, url_base_site))
            if isinstance(url_from_parse, set) and len(url_from_parse) > 0:
                res_url[cat] = url_from_parse
            sleep(randint(2,3))
        for cat, urls in res_url.items():
                for url in urls:
                        try:
                            *result, = page_parser(url, cat)
                            if len(result) == 8:
                                 save_response(*result)
                            else:
                                 print(result)
                        except TypeError as te:
                            print(*result)
                            print(f'Ошибка: {te}')
                            exit()                 
                sleep(randint(2,3))

if __name__ == '__main__':
    page_fliper(sravni_categories)
