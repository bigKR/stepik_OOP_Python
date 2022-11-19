class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    ex = ()

    def str_info(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items() if k not in self.ex)

    def __repr__(self):
        return self.str_info()

    def __str__(self):
        return self.str_info()


class ShopUserView(ShopGenericView):
    ex = ('_id',)


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

