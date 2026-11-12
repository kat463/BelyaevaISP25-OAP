n = int(input())
a = 1
b = 1
while a <= n:
    for i in range(b):
        if a <= n:
            print(a, end=" ")
            a += 1
    print()
    b += 1