x = input()
if x == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(s)
elif x == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a*b)
elif x == "круг":
    r = float(input())
    pi = 3.14
    print (pi*r**2)
