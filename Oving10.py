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
    prioritet = i = 1
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
    nyadresse = int(input("Skriv inn adresse:"))
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
        return 'Avtale ' + str(self.tittel)+'/'+ str(self.sted)+'/'+ int(self.starttidspunkt)+':'+int(self.varighet)+'/'+int(self.kategori)


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

##############################

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

#n












###########################################################################

#n

def lag_avtale():
    tittel = input("Skriv inn hva avtalen gjelder: ")
    sted = str(input("Skriv sted: "))
    dato = input("Skriv inn starttidspunkt. Skriv på format: YYYY-MM-DD TT:MM:SS")
    starttidspunkt = datetime.fromisoformat(dato)
    varighet = int(input("Skriv varighet på avtalen: "))
    DinAvtale = Avtale(tittel, sted, starttidspunkt, varighet)
    return DinAvtale

##########################################################################

#La stå nederst

if __name__ =="__main__":
    kategori_tom = []
    kategori_tom.append(lag_kategori())
    kategorier(kategori_tom)
    kategori_til_tekstfil(kategori_tom)
