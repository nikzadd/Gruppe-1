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
    nyadresse = input("Skriv inn adresse:")
    nyttSted = Kategori(nyid, nynavn, nyadresse)
    return nyttSted

############################################

#i

def nyesteder(avtaler):
    stedfil = open("stedfil.txt", "w", encoding="UTF8")
    stedfil.write("Indeks: " + "ID: "  + "Navn: " + "Adresse: " + "Ny Adresse" + "\n")
    for avtale in avtaler:
        stedfil.write(str(str(avtale.nyid) + "; " + str(avtale.nynavn) + "; " + str(avtale.nyadresse) + ";" + str(avtale.nyttsted) + "; " +"\n"))







#################################


#La stå nederst

if __name__ =="__main__":
    kategori_tom = []
    kategori_tom.append(lag_kategori())
    kategorier(kategori_tom)
    kategori_til_tekstfil(kategori_tom)