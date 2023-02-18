import collections
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
dict_res = {}
for s in students:
    if dict_res.get(s['first_name'], None):
        dict_res[s['first_name']] += 1
    else:
        dict_res[s['first_name']] = 1
for k, v in dict_res.items():
    print(f'{k}: {v}')
print(10 * '*')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
dict_name = {}
for s in students:
    if dict_name.get(s['first_name'], None):
        dict_name[s['first_name']] += 1
    else:
        dict_name[s['first_name']] = 1
max_v = max(dict_name.values())
# print(max_v)
for k, v in dict_name.items():
    if v == max_v:
        print(f'Самое частое имя среди учеников: {k}')
print(10 * '*')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

def dict_fname(st):
    dict_name = {}
    for s in st:
        if dict_name.get(s['first_name'], None):
            dict_name[s['first_name']] += 1
        else:
            dict_name[s['first_name']] = 1
    max_v = max(dict_name.values())
# print(max_v)
    for k, v in dict_name.items():
        if v == max_v:
            return k

for i in range(len(school_students)):
    print(f'Самое частое имя в классе {i+1}: {dict_fname(school_students[i])}')
print(10 * '*')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def get_nums_girls_and_boys(students):
    gils, boys = 0, 0
    for one_student in students:
        if is_male[one_student["first_name"]]: 
            boys += 1
        else: 
            gils += 1
    return(gils, boys)

for one_class in school:
    girls,boys = get_nums_girls_and_boys(one_class["students"])
    print(f'В классе {one_class["class"]} {girls} девочки и {boys} мальчика.')
print(10 * '*')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

genders = {}
for one_class in school:
    girls,boys = get_nums_girls_and_boys(one_class["students"])
    genders[one_class['class']] = [girls, boys]

girl_max = []
boys_max = []
for k, v in genders.items():
    girl_max.append(genders[k][0])
    boys_max.append(genders[k][1])
gerls_val_max = max(girl_max)
boys_val_max = max(girl_max)

for k, v in genders.items():
    if genders[k][0] == gerls_val_max:
        print(f"Больше всего девочек в классе {k}")
    if genders[k][1] == boys_val_max:
        print(f"Больше всего мальчиков в классе {k}")
