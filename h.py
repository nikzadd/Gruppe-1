
def avtale_til_tekstfil(avtaler):
    i = 0
    avtalefil = open("avatalefil.txt", "a", encoding="UTF8")
    for avtale in avtaler:
        #avtalefil.write()
        avtalefil.write(str(str(i+1) + "; " + avtale.tittel + "; " + avtale.sted + "; " +
             str(avtale.starttidspunkt) + "; " + str(avtale.varighet) + "\n"))
        i = i+1
