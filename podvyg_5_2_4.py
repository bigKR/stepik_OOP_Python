a, b = input().split()
try:
    s = int(a) + int(b)
except ValueError:
    try:
        s = float(a) + float(b)
    except ValueError:
        s = a + b
finally:
    print(s)