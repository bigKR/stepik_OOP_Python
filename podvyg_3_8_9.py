"""Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)
где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). В объектах
класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется
исключение:

raise ValueError('превышен суммарный вес предметов')
Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')"""


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []
        self.current_weight = 0

    def check_index(self, indx):
        if not isinstance(indx, int) or not -len(self.bag) <= indx <=len(self.bag):
            raise IndexError('неверный индекс')

    def check_weight(self, item, new_weight):
        if isinstance(item, Thing) and new_weight <= self.max_weight:
            self.current_weight = new_weight
            return True
        else:
            return False

    def add_thing(self, thing):
        n_w = self.current_weight + thing.weight
        if self.check_weight(thing, n_w):
            self.bag.append(thing)
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item):
        self.check_index(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        n_w = self.current_weight - self.bag[key].weight + value.weight
        if self.check_weight(value, n_w):
            self.bag[key] = value
        else:
            raise ValueError('превышен суммарный вес предметов')
        
    def __delitem__(self, key):
        self.check_index(key)
        del self.bag[key]

