#from 2d import lag_kategori

def lag_kategori():
    id = input("Skriv inn ID: ")
    navn = str(input("Skriv navn: "))
    prioritet = int(input("Skriv inn prioritet. Skriv på format: "))
    prioritet = i = 1
    Dinkategori = Kategori(id, navn, prioritet)
    return Dinkategori

def kategorier()

def kategori_fra_kategorifil(kategorier):
    i = 0
    avtalefil = open("avtalefil.txt", "w", encoding="UTF8")
    avtalefil.write("Avtalenummer: " + "Tittel: " + "Sted: " + "Starttidspunkt: " + "Varighet: " + "\n")
    for avtale in avtaler:
        avtalefil.write(str(str(i+1) + "; " + avtale.tittel + "; " + avtale.sted + "; " +
             str(avtale.starttidspunkt) + "; " + str(avtale.varighet) + "\n"))
        i = i+1


def lesing_av_kategorier():
    kategorifil = open("kategorifil", "r")
    kategorifil.readline()
    for linje in kategorifil:
        try:
            splitte = linje.strip().split(";")
            avtale = Avtale(splitte[1], splitte[2], splitte[3], splitte[4])
            print(avtale)
        except ValueError:
            continue


#g

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

#h

def avtale_til_tekstfil(avtaler):
    i = 0
    avtalefil = open("avtalefil.txt", "w", encoding="UTF8")
    avtalefil.write("Avtalenummer: " + "Tittel: " + "Sted: " + "Starttidspunkt: " + "Varighet: " + "\n")
    for avtale in avtaler:
        avtalefil.write(str(str(i+1) + "; " + avtale.tittel + "; " + avtale.sted + "; " +
             str(avtale.starttidspunkt) + "; " + str(avtale.varighet) + "\n"))
        i = i+1
#########################################




