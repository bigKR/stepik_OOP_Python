"""Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным
атрибутам объектов дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости. Объекты этого класса должны создаваться
командой:

pt = Point(x, y)
где x, y - целые или вещественные числа.

Пример использования классов (эти строчки в программе не писать):

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10"""


class ItemAttrs:
    _types = ()

    def check_value(self, value):
        if not isinstance(value, self._types):
            raise TypeError

        return value

    def check_index(self, indx):
        if not -len(self.__dict__) <= indx < len(self.__dict__):
            raise IndexError

    def __getitem__(self, item):
        self.check_index(item)
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        key = list(self.__dict__.keys())[key]
        self.__dict__[key] = self.check_value(value)


class Point(ItemAttrs):
    _types = (int, float, )

    def __init__(self, x, y):
        self.x, self.y = x, y



pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
print(x, y)
pt[0] = 10
print(pt.__dict__)