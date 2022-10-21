"""Подвиг 6. Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных)
списков следующей структуры:

lst = [[x00],
       [x10, x11],
       [x20, x21, x22],
       [x30, x31, x32, x33],
       ...
      ]
Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:

it = TriangleListIterator(lst)
где lst - ссылка на перебираемый список.

Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
Итератор должен перебирать элементы списка по указанной треугольной форме. Даже если итератору на вход будет передан
прямоугольная таблица (вложенный список), то ее перебор все равно должен осуществляться по треугольнику. Если же это
невозможно (из-за структуры списка), то естественным образом должна возникать ошибка IndexError: index out of range
(выход индекса за допустимый диапазон)."""


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]