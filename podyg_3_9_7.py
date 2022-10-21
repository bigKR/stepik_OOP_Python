class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 1
        if self.n < len(self.lst):
            return self.lst[self.n][self.column]
        raise StopIteration



lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]
s = IterColumn(lst,1)
for i in s:
    print(i)