# source env_bottom/bin/activate

import requests as re

url_all_week = 'http://localhost:5000//bottom/api/v1.0/weeklyfeedback'
url_all_categories_week = 'http://127.0.0.1:5000//bottom/api/v1.0/weeklyfeedback/category'

def get_weekly_bottom(url=url_all_week):
    sorted_dict = {}
    res = re.get(url).json()
    sorted_keys = sorted(res['weeklyfeedback'], key=res['weeklyfeedback'].get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = res['weeklyfeedback'][key]
    return sorted_dict

def get_all_categories_week(url=url_all_categories_week):
    sorted_dict_all = {}
    res = re.get(url).json()
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


