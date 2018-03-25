a = [int(i) for i in input().split()]
k = []
a1 = a[0]
t = 0
#k1 = 0
for j in a:
    if len(a) == 1: #условие для одного элемента
            k += [a1]
            break
#    if len(a) == 2: #условие если 2 числа (костыль)
#       k = reversed(a)
#       break
    if a[t] == a[-1]: #условие для последнего элемента
        a1 = a[t-1] + a[0]
    else:
        a1 = a[t-1] + a[t+1]
    k += [a1]
    t +=1
#for q in k: #вывод списка в целые числа через пробел
#    k1 = q
#    print(k1, end=' ')
print(*k)
