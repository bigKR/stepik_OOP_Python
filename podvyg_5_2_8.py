"""Подвиг 8. Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:

r = Rect(x, y, width, height)
где x, y - координаты верхнего левого угла (любые числа); width, height - ширина и высота прямоугольника
(положительные числа).

В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и
соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные числа, то
генерировать исключение командой:

raise ValueError('некорректные координаты и параметры прямоугольника')
В классе Rect реализовать метод:

def is_collision(self, rect): ...

который проверяет пересечение текущего прямоугольника с другим (с объектом rect). Если прямоугольники пересекаются, то
должно генерироваться исключение командой:

raise TypeError('прямоугольники пересекаются')
Сформировать в программе несколько объектов класса Rect со следующими значениями:

0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1

Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, в котором
должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.

P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат
(как в этом подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней грани второго,
или нижняя грань первого прямоугольника выше верхней грани второго. И то же самое для вертикальных граней."""


class Rect:
    def __init__(self, x, y, width, height):
        self._x, self._y = x, y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if key in ('_x', '_y') and type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height') and (type(value) not in (int, float) or value <= 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        r_ranges = (self._x, self._x + self._width), (rect._y - rect._height, rect._y)
        s_coords = ((self._x, self._y), (self._x, self._y - self._height),
                    (self._x + self._width, self._y), (self._x + self._width, self._y - self._height))
        for coord in s_coords:
            if r_ranges[0][0] <= coord[0] <= r_ranges[0][1] and r_ranges[1][0] <= coord[1] <= r_ranges[1][1]:
                raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_collision = set()

for r in lst_rect:
    for r2 in lst_rect:
        if r != r2 and r2 not in lst_collision:
            try:
                r.is_collision(r2)
            except TypeError:
                lst_collision.add(r2)
lst_not_collision = list(set(lst_rect) - lst_collision)
