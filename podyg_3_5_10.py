"""Подвиг 10. Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно найти
ровно один равный объект из второго ящика)."""


class Thing:
    def __init__(self, name, mass):
        self.name = name.lower()
        self.mass = mass
        self.info = (self.name, self.mass)

    def __eq__(self, other):
        if isinstance(other, Thing):
            return self.info == other.info


class Box:
    def __init__(self):
        self.thing_box = []

    def add_thing(self, obj):
        self.thing_box.append(obj)

    def get_things(self):
        return self.thing_box

    def __eq__(self, other):
        if isinstance(other, Box):
            if len(self.thing_box) != len(other.thing_box):
                return False
            else:
                b1 = sorted(self.thing_box, key=lambda x: x.info[1])
                b2 = sorted(other.thing_box, key=lambda x: x.info[1])
                return b1 == b2

