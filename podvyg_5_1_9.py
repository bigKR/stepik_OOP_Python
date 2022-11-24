class Triangle:
    def __init__(self, a, b, c):
        self.is_triangle(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def check_value(value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def check_sides(two_s, s):
        return two_s > s

    def is_triangle(self, a, b, c):
        sides = a, b, c
        for i in sides:
            self.check_value(i)

        if not all(map(lambda x: self.check_sides(sum(sides) - x, x), sides)):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []

for i in input_data:
    try:
        lst_tr.append(Triangle(*i[:3]))
    except (ValueError, TypeError):
        pass