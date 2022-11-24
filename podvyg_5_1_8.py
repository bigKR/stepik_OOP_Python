def transform_value(v):
    try:
        return int(v)
    except ValueError:
        pass

    try:
        return float(v)
    except ValueError:
        pass

    return v


lst_in = input().split()
lst_out = list(map(transform_value, lst_in))