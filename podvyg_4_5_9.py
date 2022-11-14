class PointTrack:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"{self.__class__.__name__}: {self.x}, {self.y}"

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')

        self.__dict__[key] = value


class Track:
    def __init__(self, *args):
        if len(args) == 2 and all(isinstance(x, (int, float)) for x in args):
            self.__points = PointTrack(*args)
        else:
            self.__points = args

    @property
    def points(self):
        return self.__points

    def add_back(self, pt):
        self.__points = tuple(list(self.__points) + [pt])

    def add_front(self, pt):
        self.__points = tuple([pt] + list(self.__points))

    def pop_back(self):
        if self.__points:
            last_p = self.__points[-1]
            self.__points = self.__points[:-1]
            return last_p

        return

    def pop_front(self):
        if self.__points:
            first_p = self.__points[0]
            self.__points = self.__points[1:]
            return first_p

        return


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
