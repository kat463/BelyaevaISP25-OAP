n = int(input())
h = 0
r = 0
for a in range(1, n +1):
    tun = int(input())
    min = 1000000 #????
    for b in range (tun):
        he= int(input())
        if he < min:
            min = he
    if min > h:
        h = min 
        r = 1
print(r, h)