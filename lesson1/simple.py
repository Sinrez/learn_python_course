def sum_dgt():
    a = 2
    b = 0.5
    print(a + b)

def hello(name):
    print(f"Привет, {name}!")

def digits():
    try:
        v = int(input('Введите число от 1 до 10: '))
        if 1<=v<=10:
            print(v+10)
        else:
            print('Число должно быть от 1 до 10 включительно!')
    except ValueError as vl:
        print(f'Нужно ввести число! {vl}')

def how_are_you():
    name = input('Введите ваше имя: ').strip().capitalize()
    print(f'Привет, {name}! Как дела?')

def types():
    print(float('1'))
    # print(int('2.5')) # - ValueError
    print(bool(1))
    print(bool(''))
    print(bool(0))


if __name__ == '__main__':
    sum_dgt()
    print()
    hello('Alex')
    print()
    # digits()
    print()
    # how_are_you()
    print()
    types()
