minfil = open("avtalefil.txt", "r")

def lesing_av_fil(minfil):
    for linje in minfil:
        try:
            split = linje.strip().split(";")
        except ValueError:
            print(linje)





