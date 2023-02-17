"""
Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime
"""
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, "ru_RU")

def date_work():
    str_in = "01/01/25 12:10:03.234567"
    date_of_str = datetime.strptime(str_in,'%d/%m/%y %H:%M:%S.%f').strftime('%Y-%m-%d')
    dt_now = datetime.now()
    delta1 = timedelta(days=1)
    print(f"Сегодня: {dt_now.strftime('%A %d %B %Y')}")
    print(f"Вчера: {(dt_now-delta1).strftime('%Y-%m-%d')}")
    print(f"30 дней назад: {(dt_now-(delta1*30)).strftime('%Y-%m-%d')}")
    print(f"Строка {str_in} в дату: {date_of_str}")

if __name__ == '__main__':
    date_work()