class Digit:
    type_v = (int, float)

    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if not isinstance(value, self.type_v):
            raise TypeError('значение не соответствует типу объекта')

        self.__dict__[key] = value


class Positive(Digit):
    def __setattr__(self, key, value):
        if not 0 < value:
            raise TypeError('значение не соответствует типу объекта')

        super().__setattr__(key, value)


class Negative(Digit):
    def __setattr__(self, key, value):
        if not 0 >= value:
            raise TypeError('значение не соответствует типу объекта')

        super().__setattr__(key, value)


class Integer(Digit):
    type_v = int


class Float(Digit):
    type_v = float


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = (PrimeNumber(345), PrimeNumber(1000), PrimeNumber(2), FloatPositive(0.3), FloatPositive(123.8),
          FloatPositive(45.0), FloatPositive(11.5), FloatPositive(2509.8))


lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

print(lst_positive, lst_float, sep='\n')


