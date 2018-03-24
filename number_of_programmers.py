n = int(input())
0 <= n <= 1000
if n%10 == 1:
    if n%100 == 11:
        print(n, "программистов")
    else:
        print(n, "программист")
elif n%10 == 2 or n%10 == 3 or n%10 == 4:
    if n%100 == 12 or n%100 == 13 or n%100 == 14:
        print(n, "программистов")
    else:
        print(n, "программиста")
else:
    print(n, "программистов")
