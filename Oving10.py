from h import avtale_til_tekstfil
from f import lag_avtale
from g import avtaler
from i import lesing_av_fil
import datetime as datetime

#c

class Kategori:
    def __init__(self, id=None, navn=None, prioritet=1):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet
        
    def __str__(self):
        return 'Kategori ' +str(self.id)+'/'+str(self.navn)+'/'+int(self.prioritet)
        
    
    def __str__ (self):
        return f"id: {self.id}, navn: {self.navn}, prioritet: {self.prioritet} "

##################################################################################
#d

def lag_kategori():
    id = input("Skriv inn ID: ")
    navn = str(input("Skriv navn: "))
    prioritet = int(input("Skriv inn prioritet. Skriv på format: "))
    Dinkategori = Kategori(id, navn, prioritet)
    return Dinkategori

if __name__ =="__main__":
    lag_kategori()

##########################################################################

#e & f

def kategorier(avtaleliste, overskrift="Kategori:"):
    i = 0
    print(overskrift)
    for linje in range(len(avtaleliste)):
        print("Indeks:", i+1, "ID:", avtaleliste[i].id, "Navn:", avtaleliste[i].navn, "Prioritet:",
              avtaleliste[i].prioritet)
        i = i+1

def kategori_til_tekstfil(avtaler):
    kategorifil = open("kategorifil.txt", "w", encoding="UTF8")
    kategorifil.write("Indeks: " + "ID: "  + "Navn: " + "Prioritet: " + "\n")
    for avtale in avtaler:
        kategorifil.write(str(str(avtale.id) + "; " + str(avtale.navn) + "; " + str(avtale.prioritet) + "; " +"\n"))


##########################################################################


#g

class Sted:
    def __init__(self, id = None, navn = None, adresse = None):
        self.id = id
        self.navn = navn
        self.adresse = adresse

#    def __str__(self):
#        return 'Sted ' + str(self.id + self.navn + self.adresse)

    def __str__(self) -> str:
        return f"Id: {self.id}, stedsnavn: {self.sted}, adresse: {self.adresse}"

##########################################################################

#h
def nytt_sted():
    nyid = str(input("Skriv inn id: "))
    nynavn = input("Skriv navn: ")
    nyadresse = str(input("Skriv inn adresse:"))
    nyttSted = Kategori(nyid, nynavn, nyadresse)
    return nyttSted

############################################

#i

def nyesteder(steder):
    stedfil = open("stedfil.txt", "w", encoding="UTF8")
    stedfil.write("Indeks: " + "ID: "  + "Navn: " + "Adresse: " + "Ny Adresse" + "\n")
    for sted in steder:
        stedfil.write(str(str(sted.nyid) + "; " + str(sted.nynavn) + "; " + str(sted.nyadresse) + ";" + str(sted.nyttsted) + "; " +"\n"))

############################################################################

#j

def steder(avtaleliste, overskrift = "Steder: "):
    i = 0
    print(overskrift)
    for linje in range(len(avtaleliste)):
        print("Indeks:", i+1, "Id:", avtaleliste[i].id, "Navn:", avtaleliste[i].navn, "Adresse:", avtaleliste[i].adresse)
        i += 1






#################################

#k

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet, kategori):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        self.kategori = kategori
    def __str__(self):
        return 'Avtale ' + str(self.tittel)+'/'+ str(self.sted)+'/'+ str(self.starttidspunkt)+':'+str(self.varighet)+'/'+str(self.kategori)


tittel = input ( " Skriv inn avtale")
sted = input ( " Vennligst skriv sted")
sted = str(sted)
starttidspunkt = input ( " Vennligst skriv starttidspunkt")
starttidspunkt = int(starttidspunkt)
varighet = input ( " Vennligst skriv inn varighet")
varighet = int(varighet)
kategori = input ('Hvilken kategori tilhører avtalen')
kategori = str(kategori)

DinAvtale = Avtale(tittel, sted, starttidspunkt, varighet, kategori)
print(DinAvtale)


#L

def avtale_til_tekstfil(avtaler):
    with open("avtalefil.txt", "w", encoding="UTF-8") as avtalefil:
        avtalefil.write("Avtalenummer: " + "Tittel: " + "Sted: " + "Starttidspunkt: " + "Varighet: " + "\n")
        streng = ""
        for avtale in avtaler:
            streng += f"{avtale.tittel};{avtale.sted.id};{avtale.starttidspunkt};{avtale.varighet};"
            for kategori in avtale.kategorier:
                streng += f"{kategori.id},"
        
        streng += "\n"
        avtalefil.write(streng)
     
    #"tittel;stedid;starttidspunkt;varighet;katid1,katid2,katid3"


#######################################

#m, o og p

from datetime import datetime

liste_med_avtaler = []
liste_med_steder = []
liste_med_kategorier = []

meny_valg = {
    1: "Lese inn avtaler fra fil",
    2: "Skrive avtale til fil",
    3: "Skrive inn en ny avtale",
    4: "Skrive ut alle avtalene",
    5: "Slette en avtale",
    6: "Redigere en avtale",
    7: "Avslutte",
    8: "Sjekke samme dato",
    9: "Legge til katergori",
    10: "Legge til sted",
    11: "Finne avtaler på et bestemt sted"
}


def print_meny():
    for valget in meny_valg.keys():
        print(valget, "--", meny_valg[valget])


def valg1():
    lesing_av_fil()


def valg2():
    avtale_til_tekstfil(liste_med_avtaler)


def valg3():
    liste_med_avtaler.append(lag_avtale())


def valg4():
    avtaler(liste_med_avtaler)


def valg5():
    valget = int(input("Hvilken avtale vil du fjerne? Skriv nummeret til avtalen: "))
    try:
        liste_med_avtaler.pop(valget - 1)
        avtale_til_tekstfil(liste_med_avtaler)
    except ValueError:
        print("Oisann! Det gikk ikke")
    print("Da fjernet du avtale nummer", valget)


def valg6():
    rediger_valg = int(input("Hvilken avtale vil du redigere? Skriv nummeret til avtalen: "))
    try:
        liste_med_avtaler.pop(rediger_valg - 1)
        avtale_til_tekstfil(liste_med_avtaler)
        valg3()

    except ValueError:
        pass

def valg9():
<<<<<<< Updated upstream
#print=("kategorilista")
#print=("Velg en kategori fra lista du vil legge til avtalen, ved hjelp av indeksen til kategorien")
    #kategorier(kategorifil.txt)
    with open("kategorifil.txt", "r",encoding="utf8") as kategorifil:
        linjer=kategorifil.readlines()
        for linje in linjer:
            print("Indeks",linjer.index(linje)+1, linje)
#    avtaler(liste_med_avtaler)
#    nokkelord_kategori=(input("Søk på en kategori for en avtale"))
#    with open("avtalefil.txt",'w',encoding="UTF8") as nokkelord_open:
#        linjer=nokkelord_open.readlines()
#        for linje in linjer:
#            if linje.find(nokkelord_kategori) != -1:
#                print("Avtalenummer:",linjer.index(linje)+1, linje)
valg9()
=======
    liste_med_kategorier.append(lag_kategori())

def valg10():
    liste_med_steder.append(nytt_sted())

def valg11():
    nokkelord = str(input("Skriv inn stedet du vil finne avtale til: "))
    for linje in liste_med_steder:
        if linje.find(nokkelord) != -1:
            print("Sted:",linjer.index(linje)+1, linje)
    print(nytt_sted())



def avtale_sjekk(dato, avtale_tom):
    liste_avtaler_samtidig = []
    for avtale in avtale_tom:
        if avtale.starttidspunkt == dato:  # Avtale.startidspunkt
            liste_avtaler_samtidig.append(avtale.tittel)
    return liste_avtaler_samtidig


while (True):
    print_meny()
    valg = ""
    try:
        valg = int(input("Hva ønsker du å gjøre?: "))
    except ValueError:
        print("Feil inntasting, velg et nummer:")

    if valg == 1:
        valg1()
    elif valg == 2:
        valg2()
    elif valg == 3:
        valg3()
    elif valg == 4:
        valg4()
    elif valg == 5:
        valg5()
    elif valg == 6:
        valg6()
    elif valg == 7:
        print("Takk og ha det bra!")
        break
    elif valg == 8:
        datoen = (input("Skriv inn en dato på datetime-format:"))
        datetimedato = datetime.fromisoformat(datoen)
        print(avtale_sjekk(datetimedato, liste_med_avtaler))
    elif valg == 9:
        valg9()
    elif valg == 10:
        valg10()
    elif valg == 11:
        valg11()
    else:
        print("Ugyldig valg, velg et nummer mellom 1 og 5:")

###########################################################################

#n

def lag_avtale():
    tittel = input("Skriv inn hva avtalen gjelder: ")
    stedet = input("Velg et sted fra sted-lista og skriv indeksen på stedet du vil velge:")
    sted = liste_med_steder[stedet]
    dato = input("Skriv inn starttidspunkt. Skriv på format: YYYY-MM-DD TT:MM:SS")
    starttidspunkt = datetime.fromisoformat(dato)
    varighet = int(input("Skriv varighet på avtalen: "))
    DinAvtale = Avtale(tittel, sted, starttidspunkt, varighet)
    return DinAvtale

##########################################################################
>>>>>>> Stashed changes



#La stå nederst

if __name__ =="__main__":
    kategori_tom = []
    kategori_tom.append(lag_kategori())
    kategorier(kategori_tom)
    kategori_til_tekstfil(kategori_tom)
