
def avtale_til_tekstfil(avtaler):
    i = 0
    avtalefil = open("avatalefil.txt", "a", encoding="UTF8")
    for avtale in avtaler:
        #avtalefil.write()
        avtalefil.write(str(str(i+1)[0] + "; " + avtale[1].tittel + "; " + avtale[2].sted + "; " +
             str(avtale[3].starttidspunkt) + "; " + str(avtale[4].varighet) + "\n"))
        i = i+1
