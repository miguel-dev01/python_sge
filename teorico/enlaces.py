def modifica(x, y):
    x = "xxx"
    y.append(3)
    y = y + [4]
    y[0] = 10


a = "a"
b = [0, 1, 2]
modifica(a, b)
print(a)
print(b)
