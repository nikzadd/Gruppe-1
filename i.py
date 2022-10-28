from f import Avtale


def lesing_av_fil():
    minfil = open("avtalefil.txt", "r")
    minfil.readline()
    for linje in minfil:
        try:
            splitte = linje.strip().split(";")
            avtale = Avtale(splitte[1], splitte[2], splitte[3], splitte[4])
            print(avtale)
        except ValueError:
            continue





