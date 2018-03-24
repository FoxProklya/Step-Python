a = int(input())
b = int(input())
c = 0
if a < 0 or b < 0:
    a = abs(a)
    b = abs(b)
if a == 0 or b == 0:
    print(a + b)
else:
    if a>b and a%b == 0:
        print(a)
    elif b>a and b%a == 0:
        print(b)
    elif a == b:
        print(a)
    else:
        a1 = a
        b1 = b
        #НОД, алгоритм Евклида
        while a1 != 0 and b1 != 0:
            if a1 > b1:
                a1 %= b1
            else:
                b1 %= a1
        c = a1+b1
        print(a*b//c)
