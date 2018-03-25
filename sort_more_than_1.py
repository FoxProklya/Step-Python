a = [int(i) for i in input().split()]
k = []

for i in a:
    x = int(a.count(i))
    if i in k:
        continue
    if x >= 2:
        k += [i]
k1 = sorted(k)
print(*k1)
