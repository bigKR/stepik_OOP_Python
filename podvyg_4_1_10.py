"""Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной.
Иначе, v должен быть объектом класса VectorInt."""


from operator import add, sub


class Vector:
    def __init__(self, *args):
        self.coords = args

    def len_obj_check(self, other):
        other = other.coords
        if len(other) != len(self.coords):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return self.coords

    def math_operations(self, arg1, arg2, operation):
        return tuple(operation(arg1[i], arg2[i]) for i in range(len(arg1)))

    def __add__(self, other):
        self.len_obj_check(other)
        other = other.coords
        return Vector(*self.math_operations(self.coords, other, add))

    def __sub__(self, other):
        self.len_obj_check(other)
        other = other.coords
        return Vector(*self.math_operations(self.coords, other, sub))


class VectorInt(Vector):
    value_type = int

    def __init__(self, *args):
        if not self.check_coords_type(args):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def check_coords_type(self, other):
        if isinstance(other, (Vector, VectorInt)):
            other = other.coords
        return all(map(lambda x: type(x) == self.value_type, other))

    def __add__(self, other):
        self.len_obj_check(other)
        if self.check_coords_type(other):
            other = other.coords
            return VectorInt(*self.math_operations(self.coords, other, add))
        else:
            return super().__add__(other)

    def __sub__(self, other):
        self.len_obj_check(other)
        if self.check_coords_type(other):
            other = other.coords
            return VectorInt(*self.math_operations(self.coords, other, add))
        else:
            return super().__sub__(other)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)
v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
