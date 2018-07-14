

lwr = []
mid = []
up = []

with open("buildings") as dt:
    for line in dt.readlines():
        print(line)
        tmp = input("l/m/u: ")
        if (tmp == 'l'): up.append(line)
        elif (tmp == 'm'): mid.append(line)
        elif (tmp == 'u'): lwr.append(line)
    print("Lower Campus")
    print(lwr)

    print("Middle Campus")
    print(mid)

    print("Lower Campus")
    print(up)   
