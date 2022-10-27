from f import lag_avtale
from h import avtale_til_tekstfil
def avtaler(avtaleliste, overskrift="Avtale:"):
    print(overskrift)
    for i in range(len(avtaleliste)):
        print("Avtalenummer:", i+1, "Tittel:", avtaleliste[i].tittel, "Sted:",
              avtaleliste[i].sted, "Varighet:", avtaleliste[i].varighet, "Starttidspunkt:", avtaleliste[i].starttidspunkt)
avtale_tom = []
avtale_tom.append(lag_avtale())
avtaler(avtale_tom)
avtale_til_tekstfil(avtale_tom)




