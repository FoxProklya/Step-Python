a = [i for i in input().split()]
k = [0]
t = []
r = 0
while a[0] != 'end':
    t += [[int(j) for j in a] for i in k]
    m = len(a)
    a = [i for i in input().split()]
n = len(t)
t2 = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        #if -1 <= i < n and -1 <= j < m:
        t2[i][j] += t[i-1][j] 
        t2[i][j] += t[i-n+1][j]
        t2[i][j] += t[i][j-1]
        t2[i][j] += t[i][j-m+1]
for i in range(n):
    for j in range(m):
        print(t2[i][j], end = ' ')
    print()
