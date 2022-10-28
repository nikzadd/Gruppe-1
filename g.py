from f import lag_avtale
from h import avtale_til_tekstfil

def avtaler(avtaleliste, overskrift="Avtale:"):
    i = 0
    print(overskrift)
    for linje in range(len(avtaleliste)):
        print("Avtalenummer:", i+1, "Tittel:", avtaleliste[i].tittel, "Sted:",
              avtaleliste[i].sted, "Varighet:", avtaleliste[i].varighet, "Starttidspunkt:", avtaleliste[i].starttidspunkt)
        i = i+1

if __name__ == "__main__":
    avtale_tom = []
    avtale_tom.append(lag_avtale())
    avtaler(avtale_tom)
    avtale_til_tekstfil(avtale_tom)




