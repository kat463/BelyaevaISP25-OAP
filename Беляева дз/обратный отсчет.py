k = int(input()) 
for i in range(1, k + 1):
    for sec in range(i - 1, -1, -1): 
        print(f"Осталось секунд: {sec}")
print(f"Пуск {i}")