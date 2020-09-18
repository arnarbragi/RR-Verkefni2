def runa(m):
    if m == 1:
        print(m, end = " ")
    else:
        runa(m-1)
        j = int((m * (m + 1)) / 2)
        print(j, end = " ")

        
runa(9)
