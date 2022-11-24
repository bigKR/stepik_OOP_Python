class Point:
    def __init__(self, x=0, y=0):
        self._x, self._y = x, y

    def __str__(self):
        return f"{self.__class__.__name__}: x = {self._x}, y = {self._y}"


x, y = input().split()
try:
    x, y = int(x), int(y)
    pt = Point(x, y)
except:
    try:
        x, y = float(x), float(y)
        pt = Point(x, y)
    except:
        pt = Point()
finally:
    print(pt)


