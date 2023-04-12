from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

csrf = CSRFProtect()

class LoginForm(FlaskForm):
    email = StringField('Почта пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class RegistrationForm(FlaskForm):
    first_name = StringField('Имя пользователя', validators=[DataRequired(), Length(max=100)])
    last_name = StringField('Фамилия пользователя', validators=[DataRequired(),Length(max=200)])
    user_name = StringField('Ник пользователя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

class DogForm(FlaskForm):
    name_dog = StringField('Имя собаки', validators=[DataRequired()])
    age_dog = StringField('Возраст собаки', validators=[DataRequired()])
    breed_dog = StringField('Порода собаки', validators=[DataRequired()])
    city_dog = StringField('Город', validators=[DataRequired()])
    foto_dog = StringField('Фото собаки', validators=[DataRequired()])
    voice_dog = StringField('Голос собаки', validators=[DataRequired()])
    submit = SubmitField('Отправить')
