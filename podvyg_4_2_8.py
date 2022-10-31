class IteratorAttrs:
    def __iter__(self):
        return (i for i in self.__dict__.items())


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('Samsung', (10, 20), 256)

for attr, value in phone:
    print(attr, value)

