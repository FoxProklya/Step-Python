def f(x):
    if x <= -2:
        f = 1 - (x + 2)**2
        return f
    if -2 < x <= 2:
        f = -(x/2)
        return f
    if 2 < x:
        f = (x - 2)**2 + 1
        return f

x = int(input())

print(f(x))
