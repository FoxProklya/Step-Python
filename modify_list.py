def modify_list(l):
    k = []
    for i in l:
        if i % 2 == 1:
            continue
        if i % 2 == 0:
            i //= 2
            k += [i]
    l.clear()
    l += k
    if l == []:
        l = None
