n = int(input())
m = int(input()) 
symb = input()
for r in range(n): 
    if r == 0 or r == n - 1:
        print(symb * m) 
    else:
        if m == 1:
            print(symb)
else: 
    print(symb + ' ' * (m - 2) + symb)