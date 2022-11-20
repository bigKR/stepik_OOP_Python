class Note:
    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            if not isinstance(value, str) or value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
                raise ValueError('недопустимое значение аргумента')

        if key == '_ton':
            if not isinstance(value, int) or value not in range(-1, 2):
                raise ValueError('недопустимое значение аргумента')

        self.__dict__[key] = value


class Notes:
    __instance = None
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __kyryl_names = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __new__(cls, *args, **kwargs):
        cls.__instance = object.__new__(cls) if not cls.__instance else cls.__instance

        return cls.__instance

    def __del__(self):
        self.__class__.__instance = None

    def __init__(self):
        self._do, self._re, self._mi, \
        self._fa, self._solt, self._la, self._si = (Note(self.__kyryl_names[i]) for i in range(len(self.__kyryl_names)))

    def __getitem__(self, item):
        if not isinstance(item, int) or item not in range(len(self.__slots__)):
            raise IndexError('недопустимый индекс')

        return getattr(self, self.__slots__[item])