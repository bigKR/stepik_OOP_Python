"""Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило дать вам испытание для подтверждения
уровня полученных навыков. Вам выпала великая честь создать полноценную программу игры в "Крестики-нолики". И вот перед
вами текст с заданием самого испытания.

Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса
будут создаваться командой:

game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать
исключение командой:

raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe
должны быть три публичных атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном
случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в
"Крестики-нолики" между человеком и компьютером."""


import random


class Cell:
    def __init__(self, value=0):
        if value in (0, 1, 2):
            self.value = value
        else:
            raise ValueError("ведені некоректні дані")

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.init()
        self.size = 3

    @staticmethod
    def index_check(item):
        r, c = item
        if (not isinstance(r, int) or not isinstance(c, int)) or (not 0 <= r <= 2 or not 0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.index_check(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.index_check(key)
        r, c = key
        if value == self.HUMAN_X:
            self.pole[r][c].value = value
            self.is_human_win
        elif value == self.COMPUTER_O:
            self.pole[r][c].value = value
            self.is_computer_win
        self.is_draw

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))

    def show(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.pole[r][c].value, end=' ')
            print()
        print('-----')

    def check_result(self, player=None):
        h_lines = [{self[r, c] for c in range(self.size)} for r in range(self.size)]
        v_lines = [{self[r, c] for r in range(self.size)} for c in range(self.size)]
        d_lines = [{self.pole[i][-1-i] for i in range(self.size)}, {self.pole[i][i].value for i in range(self.size)}]

        lines = [*h_lines, *v_lines, *d_lines]
        if player != self.FREE_CELL:
            return any(map(lambda x: x == {player}, lines))
        else:
            return not any(map(lambda x: player in x, lines))

    @property
    def is_computer_win(self):
        return self.check_result(player=self.COMPUTER_O)

    @property
    def is_human_win(self):
        return self.check_result(player=self.HUMAN_X)

    @property
    def is_draw(self):
        return self.check_result(player=self.FREE_CELL)

    def make_step(self, player, step_x, step_y):
        if not self[step_x, step_y]:
            self[step_x, step_y] = player
            return True
        else:
            print('Дана клітинка вже зайнята.')
            return False

    def human_go(self):
        flag = False
        while not flag:
            print('Введіть координати вашого ходу:')
            step_x, step_y = (int(i) for i in input().split())
            flag = self.make_step(self.HUMAN_X, step_x, step_y)

    def computer_go(self):
        flag = False
        while not flag:
            step_x, step_y = random.randint(0, 2), random.randint(0, 2)
            flag = self.make_step(self.COMPUTER_O, step_x, step_y)

    def __bool__(self):
        return not any([self.is_human_win, self.is_computer_win, self.is_draw])
