"""Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:

Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются).

Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

mp = MaxPooling(step=(2, 2), size=(2,2))
где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)
где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
Результатом будет таблица чисел:

6 8
9 7

P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно."""


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        big_list = []
        for i in matrix:
            big_list.extend(i)
        if len(set([len(i) for i in matrix])) != 1 or not all(map(lambda x: type(x) in (int, float), big_list)):
            raise ValueError("Неверный формат для первого параметра matrix.")
        else:
            v1, h1, v2, h2 = 0, 0, self.size[1], self.size[0]
            result = []
            m = []
            n = []
            while v2 <= len(matrix):
                if h2 <= len(matrix[0]):
                    for i in range(v1, v2):
                        m.append(max(matrix[i][h1:h2]))
                    n.append(max(m))
                    m = []
                    h1, h2 = h1 + self.step[1], h2 + self.step[1]
                else:
                    h1, h2 = 0, self.size[0]
                    v1, v2 = v1 + self.step[0], v2 + self.step[1]
                    result.append(n)
                    n = []
            return result
