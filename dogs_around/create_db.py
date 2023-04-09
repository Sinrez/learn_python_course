#это локальные костыли для доступности вспомогательных файлов, добавлять перед импортом основных библиотек
import sys
sys.path.append('..') 
sys.path.append('/Volumes/D/learn_python_course/dogs_around/webapp_dogs') 

from webapp_dogs import create_app
from webapp_dogs.model import db

app = create_app()
with app.app_context():
        db.create_all()