n = int(input())
c = 0
if 1 <= n <= 100:
    for i in range(n):
        k = int(input())
        c += k
else: print('error, input 1<n<100')
print(c)
