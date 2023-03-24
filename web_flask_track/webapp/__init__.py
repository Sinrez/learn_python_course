from flask import Flask, render_template, flash, redirect, url_for
from webapp.weather import weather_by_city
from webapp.bs_ex import get_python_news
from webapp.model import db, News, User
from webapp.forms import LoginForm
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # from . import model
    # with app.app_context():
    #     db.create_all()

    @app.route('/login')
    def login():
        title = "Авторизация"
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route("/")
    def index():
        title = 'Новостной сайт'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news)
    
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))
            
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))
    
    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))
    
    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ!'
    
    return app