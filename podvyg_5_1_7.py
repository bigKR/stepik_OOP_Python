def is_number(v):
    try:
        v = int(v)
        return v
    except ValueError:
        pass


lst_in = sum(map(int, filter(lambda x: is_number(x), input().split())))

