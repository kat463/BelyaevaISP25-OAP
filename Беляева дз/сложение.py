a = int(input())
b = int(input())
shag = int(input())
for i in range (a, b+1, shag):
    for k in range(a, b+1, shag):
        print(a , "+", b, "=", a+b, end = " ")
    print()