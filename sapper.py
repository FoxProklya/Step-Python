n, m, k = (int(i)) for i in input().split())
# создание матрицы
a = [[0 for j in range(m)] for i in range(n)]

# подсчет мин
for i in range(k):
    numstr, numstlb = (int(i) - 1 for i in input().split())
    a[numstr][numstlb] = -1

for i in range(n):
    for j in range(n):
    
        if a[i][j] == 0:
            # проверка соседних значений при 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # проверка что клетка на поле и то что ее значение == -1
                    if 0 <= ai < n and 0 <= aj < n and a[ai][aj] == -1:
                        a[i][j] +=1
                        
# вывод матрицы в квадратном виде
for i in range(n):
    for j in range(n):
        if a[i][j] == -1:
            print('*', end = ' ')
        elif a[i][j] == 0:
            print('.', end = ' ')
        else:
            print(a[i][j], end = ' ')
    print()
