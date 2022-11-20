class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        obj = self.check_type_n_return_obj(other)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        obj = self.check_type_n_return_obj(other)
        obj._amplitude = self._amplitude * other
        return obj

    def check_type_n_return_obj(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        return self.__class__(self)


class Linear(Function):
    def __init__(self, *args):
        if len(args) > 1:
            self._k, self._b = args
            super().__init__()
        elif len(args) == 1:
            self.__dict__ = args[0].__dict__.copy()

    def _get_function(self, x):
        return self._k * x + self._b




f = Linear(1, 0.5)
f2 = f + 10   # изменение смещения (атрибут _bias)
y1 = f(0)     # 0.5
y2 = f2(0)    # 10.5

print(y1, y2)