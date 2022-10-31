"""Подвиг 8. Вам необходимо создать множество классов для валидации (проверки) корректности данных. Для этого ваш
непосредственный начальник (Senior) предлагает вам объявить в программе базовый класс с именем:

Validator

обеспечивающий базовый функционал для проверки корректности данных. В частности, в этом классе нужно объявить следующий
метод:

def _is_valid(self, data): ...
По задумке этот метод должен возвращать булево значение True, если данные (data) корректны и False - в противном случае.

Так как базовый класс Validator - это общий класс для всех видов проверок, то метод _is_valid() будет просто
возвращать True.
Кроме того, объекты класса Validator:

v = Validator()   # инициализатор в классе Validator прописывать не нужно
должны вызываться подобно функциям:

v(data)
и если данные (data) некорректны, то генерировать исключение:

raise ValueError('данные не прошли валидацию')
Проверка корректности выполняется с помощью метода _is_valid(). После этого, в программе нужно объявить
два дочерних класса:

IntegerValidator - для проверки, что data - целое число в заданном диапазоне;
FloatValidator - для проверки, что data - вещественное число в заданном диапазоне.

Объекты этих классов предполагается создавать командами:

integer_validator = IntegerValidator(min_value, max_value)
float_validator = IntegerValidator(min_value, max_value)
где min_value, max_value - допустимый диапазон чисел [min_value; max_value]

Также в этих классах нужно переопределить метод:

def _is_valid(self, data): ...
который бы возвращал True, если data является числом верного типа (либо int, либо float в зависимости от валидатора)
и находится в заданном диапазоне [min_value; max_value]. Иначе, возвращается False.

Пример использования классов (эти строчки в программе писать не нужно):

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError"""


class Validator:
    def is_valid(self, data):
        pass

    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')


class TypeValidator(Validator):
    _data_type = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, self._data_type) and self.min_value <= data <= self.max_value:
            return True

        return False


class IntegerValidator(TypeValidator):
    _data_type = int


class FloatValidator(TypeValidator):
    _data_type = float


