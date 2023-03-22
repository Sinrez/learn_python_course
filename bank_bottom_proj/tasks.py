# source env_bottom/bin/activate

# если глюки, то ставить так: sudo -H python3 -m pip install "celery[redis]" --upgrade 
# запуск celery -A tasks worker --loglevel=info
# celery -A tasks beat - получаем задания по расписанию для выполнения в worker celery
# celery -A tasks worker -B --loglevel=INFO - запустить параллельно worker и beat

import sys
# это локальные костыли для доступности вспомогательных файлов, добавлять перед импортом основных библиотек
sys.path.append('..') 
sys.path.append('/Volumes/D/learn_python_course/bank_bottom_proj')
sys.path.append('/Volumes/D/learn_python_course/bank_bottom_proj/webapp_bottom')

from celery import Celery
from webapp_bottom import create_app, bottom_parser
from celery.schedules import crontab

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')
#в broker протокол именно redis:// ...

@celery_app.task
def banki_content():
    with flask_app.app_context():
        bottom_parser()

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/10'), bottom_parser.s())
    # 10 мин чтобы не дудосить
    # для запуска по пятницам в 16:30
    # sender.add_periodic_task( crontab(hour=16, minute=30, day_of_week=5), bottom_parser.s())