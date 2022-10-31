"""Подвиг 7 (на повторение). Необходимо в программе объявить класс VideoItem для представления одного видео
(например, в youtube). Объекты этого класса должны создаваться командой:

video = VideoItem(title, descr, path)
где title - заголовок видео (строка); descr - описание видео (строка); path - путь к видеофайлу. В каждом объекте
класса VideoItem должны создаваться соответствующие атрибуты: title, descr, path.

Затем, нужно создать класс для формирования оценки видео в баллах от 0 до 5. Для этого нужно объявить еще один класс с
именем VideoRating, объекты которого создаются командой:

rating = VideoRating()
В каждом объекте класса VideoRating должен быть локальный приватный атрибут с именем __rating, содержащий целое число
от 0 до 5 (по умолчанию 0). А для записи и считывания значения из этого приватного атрибута должно быть объект-свойство
(property) с именем rating.

Так как атрибут __rating - это целое число в диапазоне [0; 5], то в момент присвоения ему какого-либо значения
необходимо проверять, что присваиваемое значение - целое число в диапазоне [0; 5]. Если это не так, то генерировать
исключение командой:

raise ValueError('неверное присваиваемое значение')
Далее, в каждом объекте класса VideoItem должен быть локальный атрибут rating - объект класса VideoRating.

Пример использования классов (эти строчки в программе не писать):

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError"""


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    __rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not (isinstance(value, int) and 0 <= value <= 5):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError