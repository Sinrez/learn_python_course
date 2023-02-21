class Member:
    def __init__(self, name, proffesion, birthday):
        self.__name = name
        self.__proffesion = proffesion
        self.__birthday = birthday
    
    def get_name(self):
        return self.__name
    
    def get_proffesion(self):
        return self.__proffesion
    
    def get_birthday(self):
        return self.__birthday

    def __repr__(self):
        return f'Я - {self.__name} моя профессия: {self.__proffesion}, а родился я {self.__birthday}'

class Grandfather(Member):
    def __init__(self, name, proffesion, birthday):
        super().__init__(name, proffesion, birthday)
        self.__family_level = 'grandfather'

class Father(Member):
    def __init__(self, name, proffesion, birthday):
        super().__init__(name, proffesion, birthday)
        self.__family_level = 'father'

class Mother(Member):
    def __init__(self, name, proffesion, birthday):
        super().__init__(name, proffesion, birthday)
        self.__family_level = 'mother'

class Сhild(Member):
    def __init__(self, name, proffesion, birthday):
        super().__init__(name, proffesion, birthday)
        self.__family_level = 'child'

if __name__ == '__main__':
    family = []
    family.append(Grandfather('Петр', 'Химик', 1920))
    family.append(Father('Семен', 'Инженер', 1960))
    family.append(Mother('Ольга', 'Терапевт', 1963))
    family.append(Сhild('Антон', 'Программист', 1978))
    for member in family:
        print(member.get_name())
        print(member.get_proffesion())
        print(member.get_birthday())
        print(10*'*')
