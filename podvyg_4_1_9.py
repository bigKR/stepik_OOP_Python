class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = self.__class__.__name__

    def __call__(self, *args, **kwargs):
        obj = args[0]
        self.next_layer = obj
        return self.next_layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs


class Dense(Input):
    def __init__(self, inputs, outputs, activation):
        super().__init__(inputs)
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        self.lst_for_iter = []
        obj = self.network
        while obj:
            self.lst_for_iter.append(obj)
            obj = obj.next_layer
        return iter(self.lst_for_iter)


network = Input(128)
print(network.__class__.__name__)
