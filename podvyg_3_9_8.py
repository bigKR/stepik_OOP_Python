"""Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:



Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1,
где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')"""


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    INDX = -1

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if not self.top:
            self.top, self.INDX = obj, 0
        else:
            some_obj = self.top
            while some_obj.next:
                some_obj = some_obj.next
            some_obj.next = obj
            self.INDX += 1

    def push_front(self, obj):
        if self.top:
            obj.next = self.top
            self.top = obj
            self.INDX += 1
        else:
            self.top, self.INDX = obj, 0

    def check_indx(self, indx):
        if not isinstance(indx, int) or not 0 <= indx <= self.INDX:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        obj = self.top
        for i in range(len(self)):
            if i == item:
                return obj.data
            else:
                obj = obj.next

    def __setitem__(self, key, value):
        self.check_indx(key)
        obj = self.top
        for i in range(len(self)):
            if i == key:
                obj.data = value
                break
            obj = obj.next

    def __len__(self):
        return self.INDX + 1

    def __iter__(self):
        self.lst = []
        self.it = self.top
        while self.it:
            self.lst.append(self.it)
            self.it = self.it.next
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.lst):
            return self.lst[self.i]
        raise StopIteration




