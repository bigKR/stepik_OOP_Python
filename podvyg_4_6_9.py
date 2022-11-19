from operator import add, sub


class Money:
    def __init__(self, money):
        self._money = money

    def __setattr__(self, key, value):
        if key == 'money' and type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')

        self.__dict__[key] = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


class MoneyOperators:

    def math_operations(self, other, func):
        if type(other) in (int, float):
            return self.__class__(func(self.money, other))

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(func(self.money, other.money))

    def __add__(self, other):
        return self.math_operations(other, add)

    def __sub__(self, other):
        return self.math_operations(other, sub)


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
# m = m1 + m2  # TypeError