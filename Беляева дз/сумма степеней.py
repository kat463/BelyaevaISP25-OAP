n = int(input()) 
sum = 0 
for i in range(1, n + 1): 
    p = 0 
for j in range(1, i + 1):
     if i % 2 == j % 2: 
         p += j
         sum += i ** p
print(sum)