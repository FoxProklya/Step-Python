with open('test.txt') as inf:
    a = inf.readline()
n = ''
k = ''
t = ''
t2 = ''
for i in a:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        n = i
        t = i
    if '0' <= i <= '9':
        if '0' <= t <= '9':
            t2 = t + i
            t2 = int(t2)
            t = int(t)
            k += n * (t2 - t)
            continue
        t = i
        i = int(i)
        k += n * i
with open('test1.txt', 'w') as ouf:
    ouf.write(k)
