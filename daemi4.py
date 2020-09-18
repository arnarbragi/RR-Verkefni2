def þversumma(n):
    if n == 0:
        return 0;
    else:
        return (n % 10) + þversumma(int(n / 10))

print(þversumma(5389))
