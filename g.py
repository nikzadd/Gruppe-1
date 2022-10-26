from f import lag_avtale
def avtaler(avtaleliste, overskrift="Avtale:"):
    print(overskrift)
    for i in range(len(avtaleliste)):
        print("Avtalenummer:", i+1, "Tittel:", avtaleliste[i].tittel, "Sted:",
              avtaleliste[i].sted, "Varighet:", avtaleliste[i].varighet, "Starttidspunkt:", avtaleliste[i].starttidspunkt)
avtale_tom = []
avtale_tom.append(lag_avtale())
avtaler(avtale_tom)




