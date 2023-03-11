import requests as req
from urllib.error import HTTPError, URLError
from fake_useragent import UserAgent

def check_url(in_url:str) -> None:
    """
    Функция отправляет запрос HEAD, чтобы определить, существует ли ресурс, не загружая его содержимое
    """
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    try:
        r = req.head(in_url, allow_redirects=True, headers=fake_ua)
        if r.status_code != 200:
            print(f'Запрошенный ресурс недоступен, код: {r.status_code}')
    except req.exceptions.MissingSchema:
        print('Invalid URL')
    except HTTPError as ht_er:
        print(f'Проблема с доступностью ресурса: {ht_er}')
    except URLError as url_er:
        print(f'Ресурс-источник не найден, нужно проверить: {url_er}')
    except Exception as ex_url:
        print(f'Другая Ошибка формата запрашиваемого ресурса {ex_url}')