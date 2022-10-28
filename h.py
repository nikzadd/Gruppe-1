
def avtale_til_tekstfil(avtaler):
    i = 0
    avtalefil = open("avtalefil.txt", "w", encoding="UTF8")
    avtalefil.write("Avtalenummer: " + "Tittel: " + "Sted: " + "Starttidspunkt: " + "Varighet: " + "\n")
    for avtale in avtaler:
        avtalefil.write(str(str(i+1) + "; " + avtale.tittel + "; " + avtale.sted + "; " +
             str(avtale.starttidspunkt) + "; " + str(avtale.varighet) + "\n"))
        i = i+1
