a = input('Введите буквы и колличество повторов.(ДО 99) Пример: a3n7g22E5...')
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
