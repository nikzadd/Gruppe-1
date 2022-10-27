minfil = open("avtalefil.txt", "r")

for linje in minfil:
    try:
        split = linje.strip().split(";")
    except ValueError:
        print(linje)





