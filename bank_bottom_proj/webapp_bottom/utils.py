from model import db, Feedback
from check_resource import check_url
import requests as req
from fake_useragent import UserAgent


def get_url(url_page):
    check_url(url_page)
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    try:
            resp_fe = req.get(url=url_page,  headers=fake_ua)
            resp_fe.raise_for_status()
    except (req.RequestException, ValueError) as er_net:
        return f'Сетевая ошибка: {er_net}'
    return resp_fe

