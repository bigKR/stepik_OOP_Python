"""Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5"""


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def validate(self, other):
        if not isinstance(other, (int, float)):
            other = other.ro * other.volume

        return self.ro * self.volume, other

    def __eq__(self, other):
        v1, v2 = self.validate(other)
        return v1 == v2

    def __gt__(self, other):
        v1, v2 = self.validate(other)
        return v1 > v2

    def __lt__(self, other):
        v1, v2 = self.validate(other)
        return v1 < v2



