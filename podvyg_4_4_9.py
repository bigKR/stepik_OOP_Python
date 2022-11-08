"""Подвиг 9 (на повторение). Необходимо объявить функцию-декоратор class_log для класса, которая бы создавала
логирование вызовов методов класса. Например следующие строчки программы:

vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
декорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны при использовании этого
класса. В частности, после выполнения команд:

v = Vector(1, 2, 3)
v[0] = 10
в списке vector_log должны быть два метода:

['__init__', '__setitem__']

Ваша задача реализовать декоратор с именем class_log.

Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls
Используйте этот принцип для успешного прохождения подвига."""


vector_log = []   # наименование (vector_log) в программе не менять!

def class_log(vector_log):
    def wrapper(cls):
        dict_of_methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in dict_of_methods.items():
            setattr(cls, k, upend_func(v))
        return cls

    def upend_func(func):
        def wrapper_1(self, *args, **kwargs):
            vector_log.append(func.__name__)
            return func(self, *args, **kwargs)

        return wrapper_1

    return wrapper


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

