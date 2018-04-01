a = ''
with open('test.txt') as inf:
    for line in inf:
        line = line.strip()
        a += line
        a += ' '
k = []
t = ''
r = {}
e = ''
mat = []
fiz = []
rus = []
for i in a:
    if i == ';':
        k += [t]
        t = ''
        e = k[0]
        continue
    if i == ' ':
        k += [t]
        
        q1 = int(k[1])
        q2 = int(k[2])
        q3 = int(k[3])
        mat += [q1]
        fiz += [q2]
        rus += [q3]
        sum1 = round((q1 + q2 + q3)/3, 9)
        r[e] = sum1
        t = ''
        k.clear()
        continue
    t += i
    if t in r:
        t += '1'

k += [t]
q1 = int(k[1])
q2 = int(k[2])
q3 = int(k[3])
mat += [q1]
fiz += [q2]
rus += [q3]
sum1 = round((q1 + q2 + q3)/3, 9)
r[e] = sum1
t = ''
k.clear()
q1, q2, q3 = 0, 0, 0
for i in mat:
    q1 += i
matsr = round(q1 / len(mat), 9)
for i in fiz:
    q2 += i
fizsr = round(q2 / len(fiz), 9)
for i in rus:
    q3 += i
russr = round(q3 / len(rus), 9)
for value in r.values():
    print(value)
print(matsr, fizsr, russr)
