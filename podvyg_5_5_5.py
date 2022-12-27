"""Подвиг 5. Объявите класс Box (ящик), объекты которого создаются командой:

box = Box(name, max_weight)
где name - название ящика (строка); max_weight - максимальный суммарный вес вещей в ящике (любое положительное число).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_name - ссылка на параметр name;
_max_weight - ссылка на параметр max_weight;
_things - список из вещей, хранящиеся в ящике (изначально пустой список).

В классе Box объявите метод:

def add_thing(self, obj)

для добавления новой вещи в ящик, где obj - кортеж из двух значений:

(название_вещи, вес_вещи)

Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight, то
генерировать исключение командой:

raise ValueError('превышен суммарный вес вещей')
Затем, объявите еще один класс BoxDefender, который должен работать совместно с менеджером контекста следующим образом
(эти строчки в программе не писать):

box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    ...
Здесь b - это ссылка на объект класса Box. Если при добавлении вещей возникает исключение ValueError, то объект box
должен оставаться без изменений (с теми вещами, что были до вызова менеджера контекста). Иначе, все добавленные вещи
остаются в объекте box."""


from copy import deepcopy


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        if self._things:
            all_th_weight = sum(map(lambda x: x[1], self._things)) + obj[1]
            if self._max_weight < all_th_weight:
                raise ValueError('превышен суммарный вес вещей')

        self._things.append(obj)


class BoxDefender:
    def __init__(self, box=Box):
        self.box = box
        self.copy_of_things = deepcopy(self.box._things)

    def __enter__(self):
        return self.box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.box._things = self.copy_of_things

        return False

