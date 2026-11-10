p = int(input("Сколько раз амёба делилась?"))
am = 1
for a in range(p):
    am = am *2 
    print("Через", (a +1) *3, "часов будет", am, "амёб")