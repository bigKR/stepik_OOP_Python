"""Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится
задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать
исключение командой:

raise TypeError('можно передавать только целочисленные значения')
Пример использования класса ListInteger (эти строчки в программе не писать):

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError"""


class ListInteger(list):
    def __init__(self, o):
        self.__verify(*o)
        super().__init__(o)

    def __setitem__(self, i, o):
        self.__verify(o)
        super().__setitem__(i, o)

    def append(self, o):
        self.__verify(o)
        super().append(o)

    @staticmethod
    def __verify(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError('можно передавать только целочисленные значения')
