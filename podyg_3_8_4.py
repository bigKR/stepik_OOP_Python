class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @staticmethod
    def check_value(value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.check_value(v)
        self.__value = v


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.v_lst = [self.cell() for i in range(self.max_length)]

    def check_index(self, indx):
        if not isinstance(indx, int) and not 0 <= indx < self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.check_index(item)

        return self.v_lst[item].value

    def __setitem__(self, key, value):
        self.check_index(key)

        self.v_lst[key].value = value

    def __str__(self):
        return ' '.join([str(i.value) for i in self.v_lst])

