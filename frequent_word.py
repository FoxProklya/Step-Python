a = '' #создание строки
# чтение файла (несколько строк) и их запись в одну строку a
with open('test.txt') as inf:
    for line in inf:
        line = line.strip()
        a += line

b = a.lower() #строка с нижним регистром
k = []
t = ''
for i in b: #список из строки
    if i == ' ': #убрать пробелы
        k += [t]
        t = ''
        continue
    t += i
k += [t]
count = 0 #счетчик
s = {} 
count2 = 0 #максимальный ключ словаря
for i in k: #создания словаря
    for j in k:
        if i == j:
            count += 1
    count1 = count
    if count1 >= count2: #определение максимального значения ключа
        count2 = count1
    if count1 in s: #пропуск если значения ключа совпадают
        count = 0
        continue
    s[count1] = i #запись в словарь
    count = 0
    
# записсь в строку в расчете "значение-пробел-ключ"
o = str(s[count2])
o += ' '
o += str(count2)

#запись в файл
with open('test1.txt', 'w') as ouf:
    ouf.write(o)
