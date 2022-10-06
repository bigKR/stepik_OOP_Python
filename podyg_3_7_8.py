import random


"""Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять 
игровым полем. Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса 
Cell и содержать либо число мин вокруг этой клетки, либо саму мину.



Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса 
должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole 
(используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов 
класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение 
атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint 
модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). 
Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то 
генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False, 
либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.

Пример использования классов (эти строчки в программе писать не нужно):

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()"""


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if value not in (True, False):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int) or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if value not in (True, False):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.__pole_cells = [[Cell() for i in range(self.M)] for j in range (self.N)]
        self.total_mines = total_mines

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        mines_in_pole = self.total_mines
        while mines_in_pole:
            raw = random.randint(0, self.N - 1)
            column = random.randint(0, self.M - 1)
            if not self.__pole_cells[raw][column].is_mine:
                self.__pole_cells[raw][column].is_mine = True
                mines_in_pole -= 1
        self.count_mines_around()

    def count_mines_around(self):
        box = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for i in range(self.N):
            for j in range(self.M):
                if not self.__pole_cells[i][j].is_mine:
                    self.__pole_cells[i][j].number = sum((self.__pole_cells[i + x][j + y].is_mine for x, y in box
                                                          if 0 <= i + x < self.N and 0 <= j + y < self.M))

    def open_cell(self, i, j):
        if i > self.N or j > self.M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        if not self.__pole_cells[i][j].is_open:
            self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for i in self.__pole_cells:
            print(*i, sep='\n')



