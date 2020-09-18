def summa(m):
    if m == 0:
        return m
    else:
        z = m ** 2
        return z + summa(m-1)


print(summa(5))
