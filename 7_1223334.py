n = int(input())
t = []
if n == 0:
    print(n)
else:
    for i in range(n+1):
        if i != 0:  # какой то хитров*****ый костыль 
                    # без которого не крутится for
            for j in range(i):
                if len(t) == n:
                    break
                t += [i]
    print(*t)
