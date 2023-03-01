"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    while True:
        try:
            print('Как дела?')
            resp = input('Введите ответ: ').strip()
            if resp == 'Хорошо':
                print('И это отлично!')
                break
        except KeyboardInterrupt as ki:
            print(f'Пока! {ki}')
            break
        except Exception as ex:
            print(f'Произошла ошибка {ex}')
            break
    
if __name__ == "__main__":
    hello_user()