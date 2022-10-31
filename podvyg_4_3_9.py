"""Подвиг 9 (на повторение). Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса
StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ,
то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой
символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
Пример использования класса (эти строчки в программе не писать):

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError"""


class StringDigit(str):
    def __init__(self, string):
        self.check_value(string)
        self.string = string

    def __add__(self, other):
        other = self.check_cls_n_return(other)
        return StringDigit(self.string + other)

    def __radd__(self, other):
        other = self.check_cls_n_return(other)
        return StringDigit(other + self.string)

    @staticmethod
    def check_value(value):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def check_cls_n_return(self, value):
        if isinstance(value, StringDigit):
            value = value.string
        self.check_value(value)
        return value



sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"
try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"
sd = "0" + sd
print(sd)
assert sd == "0123345", "неверно отработал оператор +"
try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
