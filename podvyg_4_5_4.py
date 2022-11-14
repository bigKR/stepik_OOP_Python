class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __id = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__class__.__id + 1

    @classmethod
    def set_id(cls):
        cls.__id += 1
        return cls.__id

    def get_id(self):
        return self.__id
