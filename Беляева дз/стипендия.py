A = float(input("Ведите стипендию"))
B = float(input("Введите расходы"))
s = 0 
for c in range(10):
    s = s + B - A
B = B * 1.03
print("Сумма от родителей", s)