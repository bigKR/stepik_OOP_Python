"""Подвиг 7. В программе выполняется считывание числовых данных из входного потока, командой:

digits = list(map(float, input().split()))
Эти данные следует представить в виде объекта класса TupleLimit. Сам класс должен наследоваться от класса tuple, а его
объекты создаваться командой:

tl = TupleLimit(lst, max_length)
где lst - коллекция (список или кортеж) из данных; max_length - максимально допустимая длина коллекции TupleLimit.
Если длина lst превышает значение max_length, то должно генерироваться исключение командой:

raise ValueError('число элементов коллекции превышает заданный предел')
В самом классе TupleLimit переопределить магические методы __str__() и __repr__() для отображения объекта класса
TupleLimit в виде строки из набора данных lst, записанных через пробел. Например:

"1.0 2.5 -5.0 11.2"

Создайте в программе объект класса TupleLimit для прочитанных данных digits и параметром max_length = 5. Выведите на
экран объект в случае его успешного создания. Иначе, выведите сообщение обработанного исключения."""


class TupleLimit(tuple):
    def __new__(cls, lst, max_lenght):
        if len(lst) > max_lenght:
            raise ValueError('число элементов коллекции превышает заданный предел')

        return super().__new__(cls, lst)

    def __str__(self):
        return f'{" ".join([str(i) for i in self])}'

    def __repr__(self):
        return str(self)


digits = list(map(float, input().split()))
try:
    s = TupleLimit(digits, 5)
    print(s)
except Exception as e:
    print(e)