"""Подвиг 3. Объявите функцию с сигнатурой:

def input_int_numbers(): ...

которая бы считывала строку из введенных целых чисел, записанных через пробел, и возвращала кортеж из введенных чисел
(в виде целых чисел, а не строк).

Если хотя бы одно значение не является целым числом, то генерировать исключение, командой:

raise TypeError('все числа должны быть целыми')
Вызовите эту функцию в цикле до тех пор, пока пользователь не введет в строке все целочисленные значения
(то есть, цикл завершается, когда функция отработает штатно, без генерации исключения).

Выведите на экран прочитанные значения, записанные в виде строки через пробел."""


def input_int_numbers():
    numbers = input().split()
    if all([i.lstrip('-').isdigit() for i in numbers]):
        numbers = tuple(eval(i) for i in numbers)
    if not all(map(lambda x: type(x) == int, numbers)):
        raise TypeError('все числа должны быть целыми')

    return numbers


while True:
    try:
        n = input_int_numbers()
    except TypeError:
        pass
    else:
        print(' '.join((str(i) for i in n)))
        break

