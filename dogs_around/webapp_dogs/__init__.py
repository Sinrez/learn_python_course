# source env_dogs/bin/activate
# ./run.sh

from flask import Flask, render_template, flash, redirect, url_for,request, session, jsonify, abort
from datetime import datetime
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm, csrf
from wtforms import StringField, SubmitField
from webapp_dogs import config
from werkzeug.security import generate_password_hash
from webapp_dogs.model import db, User, Dog, get_user_dogs, Friendship, FrendStatusEnum
from webapp_dogs.forms import RegistrationForm, DogForm , LoginForm
from webapp_dogs.utils_dog import generate_id_user, get_or_create_user, generate_id_dog, get_or_create_dog
from flask_login import LoginManager,login_user, logout_user, current_user, login_required

def create_app():
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)    

    @app.route("/")
    def index():
        title = 'Собакруг'
        dogs = Dog.query.order_by(Dog.response_date.desc()).all() 
        return render_template('index.html', page_title=title, dogs= dogs)

    @app.route("/cabinet")
    def cabinet():
        title = 'Мой профиль'
        email = session.get('email')
        dogs = Dog.query.order_by(Dog.response_date.desc()).all() 
        print(dogs)
        my_dogs = get_user_dogs(email)
        res_my_dogs = ', '.join([dog.name_dog for dog in my_dogs])
        return render_template('cabinet.html', page_title=title, dogs= dogs, my_dogs = res_my_dogs, email = email)
    
    @app.route("/profile")
    def profile():
        email = session.get('email')
        user = User.query.filter_by(email=email).first() 
        title = 'Мой профиль'

        return render_template('profile.html', page_title=title, user=user)

    @app.route('/dog/<string:dog_id>')
    def profile_dog(dog_id):
        email = session.get('email')
        dog = Dog.query.filter_by(id_dog=dog_id).first() 
        title = 'Профиль собачки'
        return render_template('profile_dog.html', page_title=title, dog=dog)

    @app.route('/add_friend/<string:dog_id>', methods=['POST'])
    @login_required
    def add_friend(dog_id):
        # user_id = session.get('user_id')
        email = session.get('email')
        my_dog = get_user_dogs(email)[0]
        dog = Dog.query.get(dog_id)
        if dog is None:
            abort(404)
        print(current_user.id_user)
        print(my_dog)
        if my_dog:
            friendship_request = Friendship(sender_dog_id=my_dog.id_dog, receiver_dog_id=dog_id)
            db.session.add(friendship_request)
            db.session.commit()
            flash(f'Вы отправили запрос на дружбу {dog.name_dog}!', 'success')
        else:
            flash('Произошла ошибка! Попробуйте еще раз.', 'danger')
        return redirect(url_for('user_dogs'))
    
    @app.route('/accept_request/<string:id_dog>')
    def accept_request(id_dog):
        request = Friendship.query.filter_by(sender_dog_id=id_dog, status=FrendStatusEnum.pending.value).first()
        if request:
            request.accept_request()
        return redirect(url_for('user_dogs'))

    @app.route('/reject_request/<string:id_dog>')
    def reject_request(id_dog):
        request = Friendship.query.filter_by(sender_dog_id=id_dog, status=FrendStatusEnum.pending.value).first()
        if request:
            request.decline_request()
        return redirect(url_for('user_dogs'))

    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        title = "Авторизация"
        form = LoginForm()
        email = None 

        if request.method == 'POST' and form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)  # авторизация пользователя
                print(user.get_mail())
                email = user.get_mail()
                session['email'] = email 
                user_id = user.get_id()
                session['user_id'] = user_id 
                flash('Вы успешно авторизовались!', 'success')
                next_page = request.args.get('next') # получаем параметр next из URL
                if next_page:
                    return redirect(next_page) # если параметр есть, переходим по нему
                else:
                    return redirect(url_for('cabinet'))
            else:
                flash('Неправильное имя пользователя или пароль', 'danger')

        return render_template('login.html', form=form, title=title, email=email)
    
    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))
    
    @app.route('/registration', methods=['GET', 'POST'])
    def registration():
        form = RegistrationForm()
        if request.method == 'POST' and form.validate_on_submit():
            # Получение данных из формы
            id_user = generate_id_user()
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            user_name = request.form['user_name']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']

            # Валидация данных
            error = None
            if not first_name:
                error = 'Имя пользователя обязательно для заполнения.'
            elif not last_name:
                error = 'Фамилия пользователя обязательна для заполнения.'
            elif not password:
                error = 'Пароль обязателен для заполнения.'
            elif password != confirm_password:
                error = 'Пароли не совпадают.'

            if error is None:
                # Сохранение данных в бд
                hashed_password = generate_password_hash(password)
                res = get_or_create_user(id_user,first_name, last_name, user_name, email, hashed_password)
                if res:
                    return redirect(url_for('login'))
            # Если данные не прошли валидацию, показываем ошибки пользователю
            return render_template('registration.html', error=error)
        else:
            print(form.errors)
        # Если метод запроса GET, просто отображаем шаблон
        return render_template('registration.html', form=form)
    
    @app.route('/user_dogs', methods=['GET'])
    def user_dogs():
        email = session.get('email') # получаем email пользователя из запроса
        print(email)
        user_dogs = get_user_dogs(email)
        print(user_dogs)
        friend_requests = [dog.get_friend_requests() for dog in user_dogs][0]
        print(f'Список запросов в друзья: {friend_requests}')
        friends = [dog.get_friends() for dog in user_dogs][0]
        print(friends)
        if user_dogs:
            return render_template('user_dogs.html', dogs= user_dogs,  email = email, friend_requests = friend_requests, friends= friends)
        else:
            return {'message': 'User not found'}, 404  # возвращаем сообщение об ошибке, если пользователь не найден

    @app.route('/register_dog', methods=['GET', 'POST'])
    @login_required
    def register_dog():
        form = DogForm()
        if request.method == 'POST' and form.validate_on_submit():
            username = current_user.email
            print(username)
            name_dog = form.name_dog.data
            age_dog = form.age_dog.data
            breed_dog = form.breed_dog.data
            response_date = datetime.now()
            city_dog = form.city_dog.data
            foto_dog = form.foto_dog.data
            voice_dog = form.voice_dog.data
            id_dog = generate_id_dog(name_dog, age_dog, breed_dog, response_date, city_dog)

            # Валидация данных
            error = None
            if not name_dog:
                error = 'Кличка собаки обязательна для заполнения.'
            elif not age_dog:
                error = 'Возраст собаки обязателен для заполнения.'
            elif not breed_dog:
                error = 'Порода обязательна для заполнения.'
            elif not city_dog:
                error = 'Город обязателе для заполнения.'

            if error is None:
                get_or_create_dog(id_dog,name_dog, age_dog, breed_dog, response_date,city_dog, foto_dog, voice_dog, username)
            flash('Респекты, ваш песель зарегистрирован!')
            return redirect(url_for('cabinet'))
        else:
            print(form.errors)
        return render_template('register_dog.html', form=form)
    return app