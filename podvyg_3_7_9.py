"""Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД. Объекты этого класса
создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по
именам полей (field_name1,... , field_nameN) с соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев
Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться
исключение командой:

raise IndexError('неверный индекс поля')
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record."""


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    @staticmethod
    def len_difference(obj1, obj2):
        if len(obj1) != len(obj2):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        if isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords

        return Vector(*map(lambda x, y: x + y, self.coords, other))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [i + other for i in self.coords]
        elif isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords
            self.coords = list(map(lambda x, y: x + y, self.coords, other))

        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords

        return Vector(*map(lambda x, y: x - y, self.coords, other))

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [i - other for i in self.coords]
        elif isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords
            self.coords = list(map(lambda x, y: x - y, self.coords, other))

        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords

        return Vector(*map(lambda x, y: x * y, self.coords, other))

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [i * other for i in self.coords]
        elif isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords
            self.coords = list(map(lambda x, y: x * y, self.coords, other))

        return self

    def __len__(self):
        return len(self.coords)

    def __eq__(self, other):
        if isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords
            res_list = all(list(map(lambda x, y: x == y, self.coords, other)))

            return res_list

    def __ne__(self, other):
        if isinstance(other, Vector):
            self.len_difference(self, other)
            other = other.coords
            res_list = any(list(map(lambda x, y: x != y, self.coords, other)))

            return res_list


v1 = Vector(4, 5, 6, 7)
v2 = Vector(1, 2, 3, 4)
v3 = v1 + v2
print(v3.coords)