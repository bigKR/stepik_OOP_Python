from itertools import chain
from random import randint


class Ship:
    _around_ship = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1))

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x, self._y = x, y
        self._cells = [1] * self._length
        self._is_move = True
        self._size_of_pole = 10

    def get_all_coords(self):
        coords = []
        for i in range(self._length):
            if self._tp == 1:
                coords.append((self._x + i, self._y))
            elif self._tp == 2:
                coords.append((self._x, self._y + i))
        return coords

    @staticmethod
    def coord_out_pole(coord, size):
        return not 0 <= coord < size

    def is_out_pole(self, size):
        coords = self.get_all_coords()
        return any((map(lambda x: self.coord_out_pole(x[0], size) or self.coord_out_pole(x[1], size), coords)))

    def set_start_coords(self, x, y):
        coords = (self._x, self._y)
        self._x, self._y = x, y
        if self.is_out_pole(self._size_of_pole):
            self._x, self._y = coords
            return False

        return True

    def get_start_coords(self):
        return self._x, self._y

    def is_collide(self, ship):
        ship_coords = ship.get_all_coords()
        my_coords = self.get_all_coords()
        if any(map(lambda x: x in ship_coords, my_coords)):
            return True

        for i in self._around_ship:
            a_x, a_y = i
            for j in my_coords:
                x, y = j
                if not self.coord_out_pole(x + a_x, self._size_of_pole) and not self.coord_out_pole(y + a_y, self._size_of_pole):
                    if (x + a_x, y + a_y) in ship_coords:
                        return True

        return False

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                return self.set_start_coords(self._x + go, self._y)
            elif self._tp == 2:
                return self.set_start_coords(self._x, self._y + go)

        return False

    def __getitem__(self, item):
        if item in range(self._length):
            return self._cells[item]

    def __setitem__(self, key, value):
        if key in range(self._length) and value in (1, 2):
            if value == 2:
                self._is_move = False

            self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = [[0] * self._size for i in range(self._size)]

    def init(self):
        self._ships = list(chain(Ship(4 - i, tp=randint(1, 2)) for i in range(4) for j in range(i + 1)))
        ships_on_pole = []

        for ship in self.get_ships():
            ship._size_of_pole = self._size
            flag = True
            while flag:
                x, y = randint(0, self._size - 1), randint(0, self._size - 1)
                if not ships_on_pole:
                    is_set = ship.set_start_coords(x, y)
                    if is_set:
                        flag = False
                        ships_on_pole.append(ship)
                else:
                    is_set = ship.set_start_coords(x, y)
                    if is_set:
                        if all(map(lambda x: not ship.is_collide(x), ships_on_pole)):
                            ships_on_pole.append(ship)
                            flag = False

    def get_pole(self):
        self._pole = [[0] * self._size for i in range(self._size)]
        for ship in self.get_ships():
            coords = ship.get_all_coords()
            for c in range(len(coords)):
                self._pole[coords[c][0]][coords[c][1]] = ship._cells[c]

        return tuple(tuple(i) for i in self._pole)

    def show(self):
        pole = self.get_pole()
        for i in pole:
            print(*i, end='\n')

    def get_ships(self):
        return self._ships

    def move_ships(self):
        step = -1
        all_ships = self.get_ships()
        for ship in all_ships:
            cur_x, cur_y = ship.get_start_coords()
            flag = False
            count = 0
            while not flag:
                if count < 2:
                    step = -step
                    flag = ship.move(step)
                    count += 1
                    # print(count)
                else:
                    break

            if count != 2:
                for s in all_ships:
                    if s != ship:
                        if ship.is_collide(s):
                            ship.set_start_coords(cur_x, cur_y)
                            break


class SeaBattle():
    def __init__(self, player1, player2=None, size=10):
        self.pole = GamePole(size)
        self.player1 = player1
        self.player2 = player2

    def play_game(self):
        w

# p = GamePole(10)
# p.init()
# for nn in range(5):
#     for s in p._ships:
#         assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
#         for ship in p.get_ships():
#             if s != ship:
#                 assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
#     p.move_ships()
#
# gp = p.get_pole()
# assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
# assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
# pole_size_8 = GamePole(8)
# pole_size_8.init()







p = GamePole(10)
p.init()
p.show()
p.move_ships()
print('', end='\n')
p.show()
