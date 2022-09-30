"""Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2
И функция:

n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track

P.S. На экран в программе ничего выводить не нужно."""


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.way = []

    def add_track(self, tr):
        if not (self.start_x and self.start_y):
            self.start_x = tr.to_x
            self.start_y = tr.to_y
        self.way.append(tr)

    def get_tracks(self):
        return tuple(self.way)

    def __eq__(self, other):
        if isinstance(other, Track):
            track1 = len(self)
            track2 = len(other)
        return track1 == track2

    def __gt__(self, other):
        if isinstance(other, Track):
            track1 = len(self)
            track2 = len(other)
        return track1 > track2

    def __len__(self):
        distance = 0
        for i in range(len(self.way)):
            if i + 1 < len(self.way):
                distance += ((self.way[i + 1].to_x - self.way[i].to_x) ** 2
                                + (self.way[i + 1].to_y - self.way[i].to_y) ** 2) ** 0.5
        return int(distance)
