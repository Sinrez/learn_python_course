"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None, random.choice([m["id"] for m in messages]) if messages else []]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

def top_msg_user(log_inp):
    """
     1. Вывести айди пользователя, который написал больше всех сообщений.
    """
    users: dict = {}
    for lo in log_inp:
        user_id = lo["sent_by"]
        users[user_id] = users.get(user_id, 0) + 1
    return f'Больше всех сообщений отправил пользователь с id = {max(users, key=users.get)}'


def top_answer_user(log_inp):
    """
    2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
    """
    uuids: dict = {}
    for lo in log_inp:
        reply_for = str(lo["reply_for"])
        if reply_for != 'None':
        # print(reply_for)
            uuids[reply_for] = uuids.get(reply_for, 0) + 1
    max_msg_uuid = max(uuids, key=uuids.get)
    for lo in log_inp: 
        if str(lo["reply_for"]) == str(max_msg_uuid):
            return f'Чаще всего отвечали пользователю с id = {lo["sent_by"]}'


def id_popular_users(log_inp):
        """
         3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
        """
        id_users: dict = {}
        for lo in log_inp:
            id_users[lo["sent_by"]] = len(set(lo["seen_by"]))
        print('Больше всего уникальных пользователей у:')
        for k, v in id_users.items():
            if v > 5:
                print(f'Пользовалтель id = {k}, число уникальных {v}')
        
def popular_time(log_inp):
    """
    4. Определить, когда в чате больше всего сообщений: 
    утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
    """
    timers = {
        'утром': 0,
        'днем' : 0,
        'вечером' : 0
    }
    for lo in log_inp:
        time_in = int(lo['sent_at'].strftime('%H:%M')[:2])
        if 4 < time_in < 12:
            timers['утром'] += 1
        elif 12 <= time_in < 18:
            timers['днем'] += 1
        else:
            timers['вечером'] += 1
    return f'Больше всего сообщений в чате {max(timers, key=timers.get)}'

    pass

def popuclar_chains(log_inp):
    """
    5. Вывести идентификаторы сообщений, 
    который стали началом для самых длинных тредов (цепочек ответов).
    """
    uuids: dict = {}
    for lo in log_inp:
        reply_for = str(lo["reply_for"])
        if reply_for != 'None':
            uuids[reply_for] = uuids.get(reply_for, 0) + 1
    print('Cтали началом для самых длинных тредов (цепочек ответов):')
    for k, v in uuids.items():
            if v > 4:
                print(f'Идентификатор: {k}, длина цепочки: {v}')

if __name__ == "__main__":
    logs = generate_chat_history()
    # print(logs)
    print(top_msg_user(logs))
    print(15*'*')
    print(top_answer_user(logs))
    print(15*'*')
    id_popular_users(logs)
    print(15*'*')
    print(popular_time(logs))
    print(15*'*')
    popuclar_chains(logs)


