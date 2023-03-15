from check_resource import check_url
import requests as req
from fake_useragent import UserAgent
UserAgent().chrome
from flask import Flask
from model import db, Feedback
from config import SQLALCHEMY_DATABASE_URI


def get_url(url_page:str):
    check_url(url_page)
    ua = UserAgent()
    fake_ua = {'User-Agent': UserAgent().chrome}
    if 'sravni' in url_page:
        try:
                resp_for_cookeis = req.get("https://www.sravni.ru/")
                resp_for_cookeis.raise_for_status()
                resp_fe = req.get(url=url_page,  headers=fake_ua, cookies=resp_for_cookeis.cookies)
                resp_fe.raise_for_status()
        except (req.RequestException, ValueError) as er_net:
            return f'Сетевая ошибка: {er_net}'
    else:
        try:
                resp_fe = req.get(url=url_page,  headers=fake_ua)
                resp_fe.raise_for_status()
        except (req.RequestException, ValueError) as er_net:
            return f'Сетевая ошибка: {er_net}'
    return resp_fe

def save_response(id_url, url_page, bank_name, category, short_feedback, response_date, response_city, response_full) -> None:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    with app.app_context():
        # @todo добавить обработку sqlalchemy.exc.OperationalError
        db.init_app(app)
        url_exists = Feedback.query.filter(Feedback.url_page == url_page).count()
        if not url_exists:
            new_feedback = Feedback(id_url=id_url, url_page=url_page, bank_name=bank_name, category=category, 
                                    short_feedback=short_feedback,response_date=response_date,response_city=response_city,
                                    response_full=response_full)
            db.session.add(new_feedback)
            db.session.commit()