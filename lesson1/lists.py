def list_1():
    lst = [3, 5, 7, 9, 10.5]
    print(*lst)
    lst.append("Python")
    print(f'Добавили {lst[-1]}. Длина списка: {len(lst)}')
    print(f'начальный элемент списка: {lst[0]}')
    print(f'последний элемент списка: {lst[-1]}')
    print(f'элементы списка со второго по четвертый: {lst[1:4]}')
    lst.remove("Python")
    print(f'После удаления: {lst}')


if __name__ == '__main__':
    list_1()