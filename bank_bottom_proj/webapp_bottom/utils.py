from model import db, Feedback
from check_resource import check_url
import requests as req
from fake_useragent import UserAgent


def save_response(id_url, url_page, bank_name, category, short_feedback, response_date, response_city, response_full):
    url_exists = Feedback.query.filter(Feedback.url_page == url_page).count()
    if not url_exists:
        new_feedback = Feedback(id_url=id_url, url_page=url_page, bank_name=bank_name, category=category, 
                                short_feedback=short_feedback,response_date=response_date,response_city=response_city,
                                response_full=response_full)
        db.session.add(new_feedback)
        db.session.commit()

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

