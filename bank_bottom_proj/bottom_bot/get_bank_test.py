import requests as re


for_test = {'weeklyfeedback': {'Альфа-Банк': 72, 'Банк «Открытие»': 62, 'Банки.ру': 15, 
                               'ВТБ': 139, 'Газпромбанк': 61, 'Драйв Клик Банк': 14, 'МТС Банк': 55, 'ОТП Банк': 17, 'Почта Банк': 20, 'Промсвязьбанк': 12, 'Райффайзен Банк': 11, 'Росбанк': 40, 'Россельхозбанк': 26, 'Сбербанк': 84, 'Совкомбанк': 57, 
                               'Тинькофф Банк': 115, 'Уралсиб': 11, 
                               'Уральский банк реконструкции и развития (УБРиР)': 16, 'Хоум Кредит Банк': 48}}

for_test_2 =  {'category': {'autocredits': {'Банк «Открытие»': 7, 'ВТБ': 20, 'Драйв Клик Банк': 14, 'Росбанк': 21, 'Совкомбанк': 13, 'Тинькофф Банк': 14}, 'creditcards': {'Альфа-Банк': 24, 'Банк «Открытие»': 6, 'Газпромбанк': 11, 'МТС Банк': 13, 'Сбербанк': 8, 'Тинькофф Банк': 9, 'Хоум Кредит Банк': 12}, 'credits': {'Альфа-Банк': 6, 'ВТБ': 6, 'Газпромбанк': 7, 'МТС Банк': 17, 'Почта Банк': 6, 'Совкомбанк': 9, 'Тинькофф Банк': 21, 'Хоум Кредит Банк': 15}, 'debitcards': {'Альфа-Банк': 14, 'Банк «Открытие»': 7, 'Банки.ру': 6, 'ВТБ': 13, 'Газпромбанк': 6, 'Сбербанк': 6, 'Тинькофф Банк': 15}, 'deposits': {'Банк «Открытие»': 8, 'Газпромбанк': 13, 'Сбербанк': 8, 'Совкомбанк': 8, 'Хоум Кредит Банк': 13}, 'hypothec': {'Банк ДОМ.РФ': 6, 'ВТБ': 49, 'Россельхозбанк': 8, 'Сбербанк': 21}, 'other': {'Альфа-Банк': 11, 'ВТБ': 12, 'Россельхозбанк': 6, 'Сбербанк': 11, 'Тинькофф Банк': 6}, 'remote': {'Банк «Открытие»': 8, 'Газпромбанк': 7, 'Сбербанк': 8, 'Тинькофф Банк': 20}, 'restructing': {'Альфа-Банк': 6, 'Банк «Открытие»': 11, 'ВТБ': 16, 'Газпромбанк': 6, 'Сбербанк': 8, 'Совкомбанк': 7, 'Тинькофф Банк': 16}, 'transfers': {'Банк «Открытие»': 8, 'МТС Банк': 8, 'Сбербанк': 12, 'Тинькофф Банк': 10}}}

url_all_week = 'http://localhost:5000//bottom/api/v1.0/weeklyfeedback'
url_all_categories_week = 'http://localhost:5000//bottom/api/v1.0/weeklyfeedback/category'

def get_weekly_bottom(url=for_test):
    sorted_dict = {}
    # res = re.get(url).json()
    res = for_test
    sorted_keys = sorted(res['weeklyfeedback'], key=res['weeklyfeedback'].get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = res['weeklyfeedback'][key]
    return sorted_dict


def get_all_categories_week(url=for_test_2):
    sorted_dict_all = {}
    res = url
    for category in res['category']:
        sorted_dict = {}
        sorted_keys = sorted(res['category'][category], key=res['category'][category].get, reverse=True)
        for key in sorted_keys:
            sorted_dict[key] = res['category'][category][key]
        sorted_dict_all[category] = sorted_dict
    return sorted_dict_all



if __name__ == '__main__':
    # get_all_categories_week('creditcards')
    # print(get_weekly_bottom(for_test))
    # print(print_weekly_bottom())
    # print(type(get_all_categories_week()))
    print(get_all_categories_week())


