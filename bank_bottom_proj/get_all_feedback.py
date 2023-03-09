from webapp_bottom import create_app
from webapp_bottom.bottom_parser import page_fliper


app = create_app()
with app.app_context():
    page_fliper()