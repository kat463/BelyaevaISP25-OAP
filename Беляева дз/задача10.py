for x in range(29):
    a = 2 * (x**2) + 29
    c = 0
    for b in range(1, a+1):
        if a % b == 0:
            c = c +1
    if c == 2:
        print(a)