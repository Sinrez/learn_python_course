# ./run.sh
# source env_bottom/bin/activate
# export FLASK_APP=webapp_bottom && flask db init

from flask import Flask, render_template
from webapp_bottom.model  import db, Feedback
from flask_migrate import Migrate
import datetime
import pandas as pd
import plotly.graph_objs as go

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
 
    @app.route("/")
    def index():
        title = 'Дно банки'
        delta = datetime.timedelta(days=7)
        now_day = datetime.date.today()
        delta_days = now_day - delta
        date_obj = datetime.datetime.strptime(str(delta_days), '%Y-%m-%d')
        formatted_date_str = date_obj.strftime('%d.%m.%Y')
        qr = db.session.query(Feedback.bank_name,db.func.count(Feedback.url_page)).filter(Feedback.response_date >= formatted_date_str).group_by(Feedback.bank_name).having(db.func.count(Feedback.url_page) > 10).order_by(db.func.count(Feedback.url_page).desc()).all()
        
        df = pd.DataFrame(qr, columns=['bank', 'feedback'])
        fig = go.Figure(data=[go.Bar(x=df['bank'], y=df['feedback'])])
        plot_div = fig.to_html(full_html=False) 
        
        return render_template('index.html', page_title=title, banks_list= qr, plot_div=plot_div)
    
    @app.route("/feedback")
    def get_feedback():
        title = 'Дно банки'
        news = Feedback.query.order_by(Feedback.response_date.desc()).all()
        return render_template('feedback.html', page_title=title, news_list=news)
    
    return app