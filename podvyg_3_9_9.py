"""Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:



Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с
соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list,
str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта
класса TableValues), должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят
за диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')"""


class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, raw, col, type_data=int):
        self.raw = raw
        self.col = col
        self.type_data = type_data
        self.table = [[Cell(0) for col in range(self.col)] for raw in range(self.raw)]

    def check_indx(self, indx):
        if (type(indx[0]) != int or type(indx[1]) != int)\
                or (not 0 <= indx[0] < self.raw or not 0 <= indx[1] < self.col):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.table[item[0]][item[1]].data

    def __setitem__(self, key, value):
        self.check_indx(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.table[key[0]][key[1]].data = value

    def __iter__(self):
        self.indx = 0
        for i in range(len(self.table)):
            self.nxt = [j.data for j in self.table[i]]
            yield self.nxt

    def __next__(self):
        if self.indx != self.col:
            obj = self.nxt[self.indx]
            self.indx += 1
            return obj




m = TableValues(3, 2)
for i in m:
    print(i)


# tb = TableValues(3, 2)
# n = m = 0
# for row in tb:
#     n += 1
#     for value in row:
#         m += 1
#         assert type(
#             value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
#
# assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"
#
# tb[0, 0] = 10
# assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"
#
# try:
#     tb[2, 0] = 5.2
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError"