"""Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по
цепочке до последнего:



Для этого в программе объявлялись два класса:

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен иметь
следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение
командой:

raise IndexError('неверный индекс')
Пример использования классов Stack и StackObj (эти строчки в программе не писать):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    INDX = 0

    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            some_obj = self.top
            while some_obj.next is not None:
                some_obj = some_obj.next
                self.INDX += 1
            some_obj.next = obj
            self.INDX += 1

    def pop(self):
        if self.top.next is None:
            self.top = None
        else:
            p_obj = self.top
            n_obj = self.top.next
            while n_obj.next is not None:
                p_obj = n_obj
                n_obj = n_obj.next
            ret_val = p_obj.next
            p_obj.next = None
            self.INDX -= 1
            return ret_val

    def check_indx(self, indx):
        if not isinstance(indx, int) or not 0 <= indx < self.INDX:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        n = 0
        if item == 0:
            return self.top
        else:
            obj = self.top
            while True:
                if obj is not None and n == item:
                    return obj
                else:
                    obj = obj.next
                    n += 1

    def __setitem__(self, key, value):
        self.check_indx(key)
        n = 0
        if key == 0:
            value.next = self.top.next
            self.top = value
        else:
            obj = self.top
            n_obj = obj.next
            n += 1
            while True:
                if n == key:
                    value.next = n_obj.next
                    obj.next = value
                    break
                else:
                    n_obj = n_obj.next
                    obj = obj.next
                    n += 1


