# ./run.sh
# source env_bottom/bin/activate
# export FLASK_APP=webapp_bottom && flask db init
import sys

#это локальные костыли для доступности вспомогательных файлов, добавлять перед импортом основных библиотек
sys.path.append('..') 
sys.path.append('/Volumes/D/learn_python_course/bank_bottom_proj/webapp_bottom') 

from flask import Flask, render_template, jsonify, request
from webapp_bottom.model  import db, Feedback
from flask_migrate import Migrate
import datetime
import pandas as pd
import plotly.graph_objs as go
from webapp_bottom.config import categories
from utils import generate_short_id_resource ,save_response
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm, csrf
from wtforms import StringField, SubmitField

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    def get_count_from_db(days=7, cat = ''):
        delta = datetime.timedelta(days)
        now_day = datetime.date.today()
        delta_days = now_day - delta
        print(delta_days)
        date_obj = datetime.datetime.strptime(str(delta_days), '%Y-%m-%d')
        formatted_date_str = date_obj.strftime('%d.%m.%Y')
        print(formatted_date_str)
        # в зависимости наличия катеогории или возвращаем все отзывы или по категориям
        if not cat:
            qr = db.session.query(Feedback.bank_name,db.func.count(Feedback.url_page)).filter(Feedback.response_date >= formatted_date_str).group_by(Feedback.bank_name).having(db.func.count(Feedback.url_page) >= 1).order_by(db.func.count(Feedback.url_page).desc()).all()
            return qr
        else:
            qr = db.session.query(Feedback.bank_name,db.func.count(Feedback.url_page)).filter(Feedback.response_date >= formatted_date_str).filter(Feedback.category == cat).group_by(Feedback.bank_name).having(db.func.count(Feedback.url_page) >= 1).order_by(db.func.count(Feedback.url_page).desc()).all()
            return qr

    @app.route('/bottom/api/v1.0/weeklyfeedback', methods=['GET'])
    #curl -i http://localhost:5000//bottom/api/v1.0/weeklyfeedback     
    def get_feedback_weekly():
        resp = dict(get_count_from_db())
        return jsonify({'weeklyfeedback': resp})
    
    @app.route('/bottom/api/v1.0/weeklyfeedback/category', methods=['GET'])
    #curl -i http://localhost:5000//bottom/api/v1.0/weeklyfeedback/category     
    def get_feed_back_week_categ():
        res = {}
        for cat in categories:
            res[cat] = dict(get_count_from_db(cat=cat))
        return jsonify({'category': res})

    @app.route("/")
    def index():
        title = 'Дно банки'
        qr = get_count_from_db()
        df = pd.DataFrame(qr, columns=['bank', 'feedback'])
        fig = go.Figure(data=[go.Bar(x=df['bank'], y=df['feedback'])])
        plot_div = fig.to_html(full_html=False)        
        return render_template('index.html', page_title=title, banks_list= qr, plot_div=plot_div)
    
    @app.route("/feedback")
    def get_feedback():
        title = 'Дно банки'
        news = Feedback.query.order_by(Feedback.response_date.desc()).all()
        return render_template('feedback.html', page_title=title, news_list=news)
    
    @app.route("/<url>")
    def get_local_feedback(url):
        title = 'Дно банки'
        news = Feedback.query.filter_by(url_page='/'+url).first()
        print(news)
        print(type(news))
        return render_template('local_feedback.html', page_title=title, news_list=news)

    @app.route("/categories")
    def get_categories(categories: list = categories):
        bank_dict = {}
        title = 'Дно банки'
        for cat in categories:
            # важно: cat=cat передаем для отбора по категориям
            qr = get_count_from_db(cat = cat)
            df = pd.DataFrame(qr, columns=['bank', 'feedback'])
            fig = go.Figure(data=[go.Bar(x=df['bank'], y=df['feedback'])])
            plot_div = fig.to_html(full_html=False)            
            bank_dict[cat] = [qr,plot_div]
        return render_template('categories.html', page_title=title, banks_dict=bank_dict)
    
    def validate_input(form, field):
        errors = []
        excluded_chars = "*?!'^+%&;/()=}][{$#"
        for char in field.data:
            if char in excluded_chars:
                errors.append(f'Символ {char} запрещен для ввода!')
        if errors:
            raise ValidationError(*errors)

    class FeedbackForm(FlaskForm):
        bank = StringField('Банк', validators=[DataRequired(), Length(min=2, max=50), validate_input])
        theme = StringField('Тема', validators=[DataRequired(), Length(min=2, max=100),validate_input])
        category = StringField('Категория', validators=[DataRequired()])
        review = StringField('Отзыв', validators=[DataRequired(), Length(min=2, max=3000),validate_input])
        city = StringField('Город', validators=[DataRequired(), Length(min=2, max=50),validate_input])
        submit = SubmitField('Отправить')

    @app.route('/post_feedback', methods=['GET', 'POST'])
    def post_feedback():
        title = 'Дно банки'
        form = FeedbackForm()
        if form.validate_on_submit():
            form.csrf_token.data = csrf.generate_csrf()
            print("Data passed validation!")
            bank = form.bank.data
            theme = form.theme.data
            category = form.category.data
            review = form.review.data
            city = form.city.data
            id_res_in = generate_short_id_resource(review)
            id_page_in = '/' + id_res_in
            response_date_in = datetime.datetime.now()
            save_response(id_res_in, id_page_in, bank, category, theme, response_date_in, city, review)
            print(f'Отзыв добавлен {id_page_in}, {review}')
            return "Отзыв отправлен!"
        else:
            print(form.errors)
        return render_template('post_feedback.html', page_title=title, form=form)
   
    return app 