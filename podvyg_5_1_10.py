class NumbValidator:
    _type = ()

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) not in self._type or not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')


class FloatValidator(NumbValidator):
    _type = float,


class IntegerValidator(NumbValidator):
    _type = int,


def is_valid(lst, validators):
    lst_out = []
    for i in lst:
        for j in validators:
            try:
                j(i)
                lst_out.append(i)
            except ValueError:
                pass
    return lst_out


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)