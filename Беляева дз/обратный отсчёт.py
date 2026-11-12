n = int(input()) 
for num in range(2, n):
    p = True
    for i in range(2, num): 
        if num % i == 0: 
            p = False
            break
        if p: 
            print(num)