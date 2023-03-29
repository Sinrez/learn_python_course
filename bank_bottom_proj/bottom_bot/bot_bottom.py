#@bank_bottom_bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import settings
from telegram import ReplyKeyboardMarkup, KeyboardButton
from get_banks import get_weekly_bottom, get_all_categories_week
import datetime

msg = 'Я - бот "Дно банки" показываю какие банки 🏦 на этой неделе пробили дно отрицательных отзывов 💩. Жмите кнопки для просмотра статистики:'

keyb = [
    [KeyboardButton('Узнать антирейтинг лидеров недели'), KeyboardButton('Узнать антирейтинг по категориям')]
]

logging.basicConfig(
    level=logging.INFO,
    filename='bot.log',
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

# Функция для обработки команды /start
def start_handler(update, context):
    print('Вызван /start')
    print(update)
    user_f_name = update.message.chat.first_name
    user_l_name = update.message.chat.last_name
    user_id = update.message.chat.id
    user_nick = update.message.chat.username
    print()
    print(f'Пришел юзер {user_f_name} {user_l_name} c id = {user_id} и username = {user_nick}')
    # Отправляем приветственное сообщение и показываем кнопки
    update.message.reply_text(msg, reply_markup=ReplyKeyboardMarkup(keyboard=keyb, resize_keyboard=True))

def button1_handler(update, context):
    dictionary = get_weekly_bottom()
    result = '\n'.join([f'{key}: {value}' for key, value in dictionary.items()])
    update.message.reply_text(str(result))
    
def button2_handler(update, context):
    dictionary = get_all_categories_week()
    categories_info = ""
    for category, val in dictionary.items():
        result = '\n'.join([f'{key}: {value}' for key, value in val.items()])
        categories_info += f"{category}:\n{result}\n"
        categories_info += "\n"
    update.message.reply_text(categories_info)

# Функция для отправки сообщения в чат для еженедельной рассылки
def send_weekly_bottom(context: CallbackContext):
    chat_id = context.job.context
    dictionary = get_weekly_bottom()
    result = '\n'.join([f'{key}: {value}' for key, value in dictionary.items()])
    context.bot.send_message(chat_id=chat_id, text=str(result))
    
# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    try:
        mybot1 = Updater(settings.TOKEN, use_context=True)
        job_queue = mybot1.job_queue
        dp = mybot1.dispatcher
        dp.add_handler(CommandHandler("start", start_handler))
        dp.add_handler(MessageHandler(Filters.regex('Узнать антирейтинг лидеров недели'), button1_handler))
        dp.add_handler(MessageHandler(Filters.regex('Узнать антирейтинг по категориям'), button2_handler))
        # Задаем расписание для отправки сообщений
        job_queue.run_daily(send_weekly_bottom, time=datetime.time(hour=13, minute=0, second=0))

        logging.info('Бот стартовал!')
        mybot1.start_polling()
        mybot1.idle()
    except Exception as ex:
        logging.info(f'Ошибка в функции main: {ex}')
        print(f'Ошибка в функции main: {ex}')

if __name__ == '__main__':
    main()