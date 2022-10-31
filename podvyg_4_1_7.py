class Singeltone:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singeltone):
    def __init__(self, name):
        if not self.__dict__:
            self.name = name


c = Game('split')
s = Game('sp')

print(c.name, s.name)