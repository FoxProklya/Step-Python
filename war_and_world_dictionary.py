a = [i for i in input().split()]
b = {}
count = 0
for i in a:
    k = i.lower()
    for j in a:
        k1 = j.lower()
        if k == k1:
            count +=1
    b[k]=count
    count = 0
for x, y in b.items():
    print(x, y)
