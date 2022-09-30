""" Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
 lst1 = ListMath() # пустой список
 lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
 
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, остальные игнорировать (если указываются в списке). Например:
 lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:
 lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).
Также с объектами класса ListMath должны работать следующие операторы:
 lst = lst + 76 # сложение каждого числа списка с определенным числом
 lst = 6.5 + lst # сложение каждого числа списка с определенным числом
 lst += 76.7  # сложение каждого числа списка с определенным числом
 lst = lst - 76 # вычитание из каждого числа списка определенного числа
 lst = 7.0 - lst # вычитание из числа каждого числа списка
 lst -= 76.3
 lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
 lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
 lst *= 5.54
 lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
 lst = 3 / lst # деление числа на каждый элемент списка
 lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, прежние списки не меняются.
При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не создается).
P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно."""


class ListMath:
    def __init__(self, lst_math=None):
        self.lst_math = [i for i in lst_math if type(i) in (int, float)] if lst_math else []

    @staticmethod
    def multiply_value(obj_1, obj_2, symbol):
        lst = obj_1[:]
        if lst:
            for i in range(len(lst)):
                lst[i] = eval(f"{lst[i]}{symbol}{obj_2}")

        return lst

    @staticmethod
    def reduce_value(obj_1, obj_2, symbol):
        lst, value = (obj_2, obj_1)[isinstance(obj_1, list)][:], (obj_1, obj_2)[isinstance(obj_2, (int, float))]
        if type(obj_1) == list:
            for i in range(len((lst))):
                lst[i] = eval(f'{lst[i]}{symbol}{value}')
        else:
            for i in range(len((lst))):
                lst[i] = eval(f'{value}{symbol}{lst[i]}')

        return lst

    def __add__(self, other):
        return ListMath(self.multiply_value(self.lst_math, other, '+'))

    def __radd__(self, other):
        return ListMath(self.multiply_value(self.lst_math, other, '+'))

    def __iadd__(self, other):
        self.lst_math = self.multiply_value(self.lst_math, other, '+')
        return self

    def __mul__(self, other):
        return ListMath(self.multiply_value(self.lst_math, other, '*'))

    def __rmul__(self, other):
        return ListMath(self.multiply_value(self.lst_math, other, '*'))

    def __imul__(self, other):
        self.lst_math = self.multiply_value(self.lst_math, other, '*')
        return self

    def __truediv__(self, other):
        return ListMath(self.reduce_value(self.lst_math, other, '/'))

    def __rtruediv__(self, other):
        return ListMath(self.reduce_value(other, self.lst_math, '/'))

    def __itruediv__(self, other):
        self.lst_math = self.reduce_value(self.lst_math, other, '/')
        return self

    def __sub__(self, other):
        return ListMath(self.reduce_value(self.lst_math, other, '-'))

    def __rsub__(self, other):
        return ListMath(self.reduce_value(other, self.lst_math, '-'))

    def __isub__(self, other):
        self.lst_math = self.reduce_value(self.lst_math, other, '-')
        return self
