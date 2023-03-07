# ./run.sh
# source env_bottom/bin/activate
# export FLASK_APP=webapp_bottom && flask db init

from flask import Flask, render_template, flash, redirect, url_for
from webapp_bottom.model  import db, Feedback
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        title = 'Дно банки'
        return render_template('index.html', page_title=title)

    
    return app