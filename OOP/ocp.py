from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    
    def __repr__(self):
        return f"<PRODUCT : {self.name} {self.color} {self.size}>"


# class ProductFilter:
    
#     def filter_by_color(self, products, color):
#         filtered_products = []
#         for p in products:
#             if p.color == color:
#                 filtered_products.append(p)
#         return filtered_products

#     def filter_by_size(self, products, size):
#         filtered_products = []
#         for p in products:
#             if p.size == size:
#                 filtered_products.append(p)
#         return filtered_products


# Задание
# Нужно написать новый споособ фильтрации (новую реализацию класса фильтр и спецификации) 
# по цвету и размеру учитывая OCP (open/closed principal) (будем использовать вместо productFilter)
# когда это получится, можно добавить в продут такой параметр как цена и
# попробовать написать фильтр по ней и в комбинациях
# фильтр должен быть классом такого вида
#class Filter:
#    def filter(self, items, spec)
# пример вызова f.filter(products, spec)
# где spec - спецификация (с ней помогу), 
# Specification можно использовать как базовый класс, 
# от которого нужно наследоваться, чтобы создать спецификации для размера и цвета (is_satisfied)
# то что тут работает позволяет нам  брать объекты спецификаций и объединять 
# их с помощью & (привет магическим методам)


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)
    
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

# постарайся понять, что тут происходит, погугли про all, map и lambda
    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

# вот так должны фильтроваться объекты фильтром
# large_blue = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)
# f.filter(products, large_blue) -> вернет подходящие продукты

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size
    
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
    

class Filter:
   def filter(self, items, spec):
       for it in items:
            if spec.is_satisfied(it):
                yield it

if __name__ == "__main__":
    # пример создания объектов и работы с фильтром
    p1 = Product("name1", Color.BLUE, Size.MEDIUM)
    p2 = Product("name2", Color.RED, Size.MEDIUM)
    p3 = Product("name3", Color.BLUE, Size.LARGE)
    p4 = Product("name4", Color.BLUE, Size.SMALL)
    pp = [p1, p2, p3, p4]

    f = Filter()
    large_blue = SizeSpecification(Size.LARGE) & ColorSpecification(Color.BLUE)
    print(*f.filter(pp, large_blue))

