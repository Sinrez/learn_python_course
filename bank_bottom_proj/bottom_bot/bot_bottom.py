#@bank_bottom_bot

from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import logging
import settings
import datetime

msg = 'Я - бот "Дно банки" показываю какие банки 🏦 на этой неделе пробили дно отрицатльных отзывов 💩'

logging.basicConfig(
    level=logging.INFO,
    filename = 'bot.log',
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

def greet_user(update, context):
    print('Вызван /start')
    print(update)
    user_f_name = update.message.chat.first_name
    user_l_name = update.message.chat.last_name
    user_id = update.message.chat.id
    user_nick = update.message.chat.username
    print()
    print(f'Пришел юзер {user_f_name} {user_l_name} c id = {user_id} и username = {user_nick}')
    update.message.reply_text(f"Привет, {user_f_name}!")
    update.message.reply_text(msg)

# def talk_to_me(update, context):
#     user_text = update.message.text 
#     user_nick = update.message.chat.username
#     print()
#     print(f'Юзер {user_nick} ввел {user_text}')
#     update.message.reply_text(f'{user_text}')

def planet_info(update, context):
    planet_name = update.message.text.split()[1]
    today = datetime.datetime.now()
    # try:
    #     planet = getattr(ephem, planet_name)(today.strftime('%Y/%m/%d'))
    #     ephem_answer = ephem.constellation(planet)
    #     logging.info(planet_name)
    #     update.message.reply_text(f'🌜Сегодня планета {planet_name} находится в созвездии {ephem_answer[1]}🌛')
    # except AttributeError as ae:
    #     update.message.reply_text(f'🌚Я не знаю такой планеты {planet_name}.🌚')
    #     logging.info(f'Ошибка c планетой: {ae}')
    #     print(f'Ошибка c планетой: {ae}')

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    try:
        mybot = Updater(settings.TOKEN, use_context=True)

        dp = mybot.dispatcher
        dp.add_handler(CommandHandler("start", greet_user))
        dp.add_handler(CommandHandler("planet", planet_info))
        # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
        
        logging.info('Бот стартовал!')
        mybot.start_polling()
        mybot.idle()
    except Exception as ex:
        logging.info(f'Ошибка в функции main: {ex}')
        print(f'Ошибка в функции main: {ex}')

# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == '__main__':
    main()