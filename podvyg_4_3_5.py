from functools import reduce


class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.list_of_realty = {}

    def check_value(self, value):
        if not isinstance(value, SellItem):
            raise ValueError(' Обєкт повинен бути класу Thing!')

    def add_object(self, obj):
        self.check_value(obj)
        self.list_of_realty.setdefault(obj.__class__.__name__, []).append(obj)

    def remove_object(self, obj):
        self.check_value(obj)
        if obj in self.list_of_realty[obj.__class__.__name__]:
            self.list_of_realty[obj.__class__.__name__].remove(obj)

    def get_objects(self):
        return reduce(lambda x, y: x + y, list(self.list_of_realty.values()))


ag = Agency("Рога и копыта")
ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
print(ag.list_of_realty)
print(ag.get_objects())
for obj in ag.get_objects():
    print(obj.name)




