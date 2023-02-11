from pprint import pprint

def dict1():
    weather = {"city": "Москва", "temperature": "20"}
    print(weather["city"])
    print('-' * 15)
    weather["temperature"] = str(int(weather["temperature"])-5)
    pprint(weather)
    print('-' * 15)
    print('Нет ключа country' if "country" not in weather.keys() else 'Есть ключ country')
    print('-' * 15)
    weather['country'] = 'Россия'
    weather['date'] = "27.05.2019"
    print(f'длина словаря {len(weather)}')
    
 
if __name__ == '__main__':
    dict1()