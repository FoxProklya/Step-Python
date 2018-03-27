b = {}
n = int(input())
for i in range(n):
    a = int(input())
    if a in b:
        b[a+2000]= b[a] #костылечек для того чтобы ключик не повторялся
        print(b[a])
        continue
    else:
        b[a] = f(a)
        print(b[a])
