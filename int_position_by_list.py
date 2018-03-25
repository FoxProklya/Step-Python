lst = [int(i) for i in input().split()]
x = int(input())
k = []
q = 0
for i in lst:
    if i == x:
        k += [q]
    q +=1
if len(k) == 0:
    print('Отсутствует')
else:
    print(*k)
