"""Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list.
В классе SoftList следует объявить необходимые магические методы так, чтобы при обращении к несуществующему элементу
(по индексу) возвращалось значение False (а не исключение Out of Range). Например:

sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False"""


class SoftList(list):
    def __getitem__(self, item):
        if item not in range(-len(self), len(self)):
            return False
        return super().__getitem__(item)


