"""
Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны
создаваться командой:

m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы
(должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
Также объекты можно создавать командой:

m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не
прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')
Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')
Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать
исключение:

raise IndexError('недопустимые значения индексов')
Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не
совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')
Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
"""


from operator import add, sub


class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            self.list_2d_check(args[0])
            self.rows, self.cols = len(args[0]), len(args[0][1])
            self.matrix = args[0]
        elif len(args) == 3:
            self.init_values_check(args[0], args[1], args[2])
            self.rows, self.cols = args[0], args[1]
            self.matrix = [[args[2] for c in range(self.cols)] for r in range(self.rows)]

    def __getitem__(self, item):
        self.indx_check(item)
        r, c = item
        return self.matrix[r][c]

    def __setitem__(self, key, value):
        self.indx_check(key)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        r, c = key
        self.matrix[r][c] = value

    def indx_check(self, indx):
        r, c = indx
        if not (isinstance(r, int) and isinstance(c, int)) or not (0 <= r < self.rows and 0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def two_mtrx_len_check(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError('операции возможны только с матрицами равных размеров')

    @staticmethod
    def init_values_check(row, col, v_s):
        v_types = (type(i) for i in (row, col, v_s))
        if not all(map(lambda x: x in (int, float), v_types)):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    @staticmethod
    def list_2d_check(list_2d):
        len_check = all(map(lambda x: len(x) == len(list_2d[0]), list_2d))
        matrix_v_check = all(map(lambda x: x in (int, float), [type(i) for j in list_2d for i in j]))
        if not len_check or not matrix_v_check:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def math_func(self, var1, var2, func):
        if isinstance(var2, Matrix):
            var2 = var2.matrix
            self.two_mtrx_len_check(var1, var2)
            new_matrix = [[func(var1[r][c], var2[r][c]) for c in range(self.cols)] for r in range(self.rows)]
        elif isinstance(var2, int):
            new_matrix = [[func(var1[r][c], var2) for c in range(self.cols)] for r in range(self.rows)]
        return self.__class__(new_matrix)

    def __add__(self, other):
        return self.math_func(self.matrix, other, add)

    def __sub__(self, other):
        return self.math_func(self.matrix, other, sub)




