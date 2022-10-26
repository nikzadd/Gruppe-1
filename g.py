from f import lag_avtale
def avtaler():
    avtaleliste = []
    avtaleliste.append(lag_avtale())
    for i in range(len(avtaleliste)):
        print("Avtalenummer:", i+1, "Tittel:", avtaleliste[i].tittel)
avtaler()




