from flask import Flask, render_template, flash, redirect, url_for
# from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('config.py')
    # db.init_app(app)
    # migrate = Migrate(app, db)

    @app.route("/")
    def index():
        title = 'Дно банки'
        return render_template('index.html', page_title=title)

    
    return app