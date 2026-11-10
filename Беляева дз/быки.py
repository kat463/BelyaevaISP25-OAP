for b in range(101):
    for k in range(101):
        for t in range(101):
            if b + k + t == 100 and 10*b + 5*k + 0.5*t == 100:
                print("Быков",b, 'Коров',k, "Телят",t)