s = str(input())
x = int(s.upper().count('c'.upper()))
y = int(s.upper().count('g'.upper()))
z = int(len(s))
k = ((x + y) / z) * 100
print(k)
