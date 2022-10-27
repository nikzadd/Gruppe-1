minfil = open("avtalefil.txt", "r")

for linje in minfil:
    try:
        split = linje.strip().split(";")
        print(linje)
    except ValueError:
        pass





