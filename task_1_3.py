n = 1

while n <= 100:
    if n == 1 or n % 10 == 1 and n != 11:
        print(n, 'процент')
    elif 4 < n < 21 or 4 < n % 10 < 10 or n % 10 == 0:
        print(n, 'процентов')
    else:
        print(n, 'процента')
    n += 1
