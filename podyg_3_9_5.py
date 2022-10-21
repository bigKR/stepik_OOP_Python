class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item < 5:
            return self.info[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < 5:
            self.info[key] = value
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        return iter(self.info)


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError