s = str(input())
s1 = s[0]
k = s[0]
i = 0
print(k, end = "")
for s1 in s:
    if s1 == k:
        i += 1
    elif s1 != k:
        print(str(i), end = "")
        k = s1
        print(k, end = "")
        i = 1
print(str(i), end = "")
