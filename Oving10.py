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

#e

def avtaler(avtaleliste, overskrift="Avtale:"):
    i = 0
    print(overskrift)
    for linje in range(len(avtaleliste)):
        print("ID:", avtaleliste[i].id, "Navn:", avtaleliste[i].navn, "Prioritet:",
              avtaleliste[i].prioritet)
        i = i+1

def avtale_til_tekstfil(avtaler):
    kategorifil = open("nyavtalefil.txt", "w", encoding="UTF8")
    kategorifil.write("ID: " + "Navn: " + "Prioritet: " + "\n")
    for avtale in avtaler:
        kategorifil.write(str(avtale.id + "; " + avtale.navn + "; " + avtale.prioritet + "; " +"\n"))
