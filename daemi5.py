def samnefnari(n, m):
    if((m % n) == 0):
        done = True
        return n
    else:
        return samnefnari(m % n, m)

print(samnefnari(8,12))
print(samnefnari(3,13))
print(samnefnari(12,60))
print(samnefnari(21,329))
