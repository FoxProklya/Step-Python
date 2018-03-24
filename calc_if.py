x = float(input())
y = float(input())
z = input()
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "/":
    if y != 0:
        print(x/y)
    else:
        print("Деление на 0!")
elif z == "*":
    print(x*y)
elif z == "mod":
    if y != 0:
        print(x%y)
    else:
        print("Деление на 0!")
elif z == "pow":
    print(x**y)
elif z == "div":
    if y != 0:
        print(x//y)
    else:
        print("Деление на 0!")
