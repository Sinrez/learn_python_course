import requests as req
from fake_useragent import UserAgent
UserAgent().chrome
from flask import Flask
from model import db, Feedback, User
from config import SQLALCHEMY_DATABASE_URI
import hashlib
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import SQLAlchemy

def get_url(url_page:str):
    ua = UserAgent()
    fake_ua = {'User-Agent': UserAgent().chrome,
            'Referer': 'https://www.ya.ru/'}
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
    try:
        with app.app_context():
            try:
                db.init_app(app)
                url_exists = Feedback.query.filter(Feedback.url_page == url_page).count()
                if not url_exists:
                    new_feedback = Feedback(id_url=id_url, url_page=url_page, bank_name=bank_name, category=category, 
                                            short_feedback=short_feedback,response_date=response_date,response_city=response_city,
                                            response_full=response_full)
                    db.session.add(new_feedback)
                    db.session.commit()
            except SQLAlchemyError as sq:
                print(f'Ошибка sqlalchemy записи в save_response в бд: {sq}')
    except Exception as ex0:
        print(f'Ошибка в utlils.save_response: {ex0}')


def generate_short_id_resource(feedb):
    # Получаем хэш от URL с использованием sha256
    hash_object = hashlib.sha256(feedb.encode())
    hex_dig = hash_object.hexdigest()

    # Оставляем только первые 8 символов хэша и возвращаем его
    short_hash = hex_dig[:8]
    return short_hash

def get_or_create_user(effective_user, chat_id) -> None:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    try:
        with app.app_context():
            try:
                db.init_app(app)
                user_exists = User.query.filter(User.id_user == effective_user.id).first()
                if not user_exists:
                    new_user = User(id_user=effective_user.id, first_name = effective_user.first_name, 
                                    last_name = effective_user.last_name,user_name = effective_user.username, chat_id = chat_id)
                    db.session.add(new_user)
                    db.session.commit()
                return user_exists
            except SQLAlchemyError as sq:
                print(f'Ошибка sqlalchemy записи пользователя tg в get_or_create_user в бд: {sq}')
    except Exception as ex1:
        print(f'Ошибка в utlils.save_response: {ex1}')

def subscribe_user(user_data):
    app = Flask(__name__)
    db = SQLAlchemy()
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    with app.app_context():
        if user_data.subscribed is False or user_data.subscribed is None:
            db.session.query(User).filter(User.id_user == user_data.id_user).update({"subscribed": True})
            db.session.flush()
            db.session.commit()

def unsubscribe_user(user_data):
    app = Flask(__name__)
    db = SQLAlchemy()
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    with app.app_context():
        if user_data.subscribed:
            db.session.query(User).filter(User.id_user == user_data.id_user).update({"subscribed": False})
            db.session.flush()
            db.session.commit()
