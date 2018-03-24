a = int(input())
b = int(input())
s = 0
y = 0
if a%3 == 1:
    a += 2
if a%3 == 2:
    a += 1
for i in range(a, b+1, 3):
    s +=i
    y += 1
k = s/y
print(k)
