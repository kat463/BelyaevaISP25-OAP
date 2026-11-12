s = int(input())
h = int(input())
for b in range(1, h + 1):
    for c in range(0, h - b + 1):
        t = h - b - c
if 20 * b + 10 * c + 5 * t == s: 
    print (f"{b} {c} {t}")