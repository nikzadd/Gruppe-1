
def avtale_til_tekstfil(avtaler):
    i = 0
    avtalefil = open("avatalefil.txt", "w", encoding="UTF8")
    for avtale in avtaler:
        avtalefil.write(str(str(i+1) + "; " + avtale.tittel + "; " + avtale.sted + "; " +
             str(avtale.starttidspunkt) + "; " + str(avtale.varighet) + "\n"))
        avtalefil.write("{}/{}/{}/{}/{}\n".format("Avtalenummer", avtale.tittel, avtale.sted, avtale.starttidspunkt, avtale.varighet))
        i = i+1
