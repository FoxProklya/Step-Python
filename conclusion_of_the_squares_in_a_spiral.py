n = int(input())
max_n = n*n
a = [[0 for j in range(n)] for i in range(n)]
step = 1
i, j = 0, 0
i_min, j_min = 0, 0
i_max, j_max = n, n
while step <= max_n:
    while j < j_max: #вправо
        a[i][j] = step
        j += 1
        step += 1
    j -=1
    i +=1
    while i < i_max: #вниз
        a[i][j] = step
        i += 1
        step += 1
    i -= 1
    i_max -= 1
    j_max -= 1
    while j > j_min: #влево
        j -= 1
        a[i][j] = step
        step +=1
    i -= 1
    i_min += 1
    while i > i_min: #вверх
        a[i][j] = step
        step += 1
        i -= 1
    j_min += 1
    
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
