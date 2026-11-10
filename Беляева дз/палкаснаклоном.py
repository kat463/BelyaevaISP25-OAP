import math
x = int(input(""))
h = int(input(""))
y = 2 
for a in range(int(1 / h) + 1):
    b = math.cos(y / x)
    b = math.degrees(b)
    print(b)
    y = y + h
