from flask import Flask
from webapp_dogs.model import db, User, Dog
from webapp_dogs.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import SQLAlchemy
import hashlib
import uuid

def generate_id_user():
    uuid_val = uuid.uuid4().bytes
    # Получаем хэш от UUID с использованием sha256
    hash_object = hashlib.sha256(uuid_val)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def generate_id_dog(name_dog, age_dog, breed_dog, response_date, city_dog):
    input_str = f"{name_dog}-{age_dog}-{breed_dog}-{response_date}-{city_dog}"
    # Получаем хэш от строки с использованием sha256
    hash_object = hashlib.sha256(input_str.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def get_or_create_user(id_user, first_name, last_name, user_name, email, hashed_password) -> None:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    try:
        with app.app_context():
            try:
                db.init_app(app)
                user_exists = User.query.filter(User.email == email).first()
                if not user_exists:
                    new_user = User(id_user=id_user, first_name=first_name, last_name=last_name, user_name=user_name, email= email, password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    return f'Пользователь с почтой {email} зарегистрирован.'
                else:
                    return f'Пользователь с почтой {email} уже зарегистрирован.'
            except SQLAlchemyError as sq:
                print(f'Ошибка sqlalchemy записи пользователя tg в get_or_create_user в бд: {sq}')
    except Exception as ex1:
        print(f'Ошибка в функции обработки данных пользователя: {ex1}')

def get_or_create_dog(id_dog, name_dog, age_dog, breed_dog, response_date,
                    city_dog, foto_dog, voice_dog, username) -> None:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    try:
        with app.app_context():
            try:
                db.init_app(app)
                user = User.query.filter_by(email=username).first()
                dog_exists = Dog.query.filter(Dog.id_dog == id_dog).first()
                if not dog_exists:
                    new_dog = Dog(id_dog=id_dog,name_dog=name_dog, age_dog=age_dog, breed_dog=breed_dog, response_date=response_date,
                    city_dog=city_dog, foto_dog=foto_dog, voice_dog=voice_dog)
                    user.dogs.append(new_dog)
                    db.session.add(new_dog)
                    new_dog.users.append(user)
                    db.session.commit()
                return dog_exists
            except SQLAlchemyError as sq:
                print(f'Ошибка sqlalchemy записи пользователя tg в get_or_create_user в бд: {sq}')
    except Exception as ex1:
        print(f'Ошибка функции обработки данных собаки: {ex1}')