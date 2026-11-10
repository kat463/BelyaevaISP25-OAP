s = int(input("Сколько дней занятий спортом?"))
d1 = 10
sum = 0
for a in range(s):
    sum = sum + d1
    d1 = d1 * 1.1
print(sum, "км")