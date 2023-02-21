"""
в питоне если сложить 1 + "2" будет  type error напиши клас, который умеет работать с разными типами. 
класс имеет атрибут value и при сложении с другими 
объектами этого типа мы складывая 1 и 2 должны получить 3 или также ошибку типа, если строка не корректна
"""
class AddUni:
    def __init__(self, val) -> None:
        self.__val = val

    def __add__(self, other):
            if self.__val.isdigit() and other.isdigit():
                 return int(self.__val) + int(other)
            elif self.__val.isalpha() and other.isalpha():
                 return self.__val + other
            elif (self.__val.count('.') == 1 and self.__val.replace('.','').isdigit()) and (other.count('.') == 1 and other.replace('.','').isdigit()):
                 return float(self.__val) + float(other)
            elif (self.__val.count('.') == 1 and self.__val.replace('.','').isdigit()) and other.isdigit():
                 return float(self.__val) + float(other)           
            elif self.__val.isdigit() and (other.count('.') == 1 and other.replace('.','').isdigit()):
                 return float(self.__val) + float(other)           
            else:
                 raise ValueError('Передано некорретное сочетание типов!')

if __name__ == '__main__':
    try:
        v_in_1 = input('Введите первое значение: ').strip()
        v_in_2 = input('Введите второе значение: ').strip()
        v1 = AddUni(v_in_1)
        print(f'Результат: {v1+v_in_2}')
    except ValueError as ve:
         print(f'Ошибка: {ve}')
    except Exception as ex:
         print(f'Ошибка {ex}')