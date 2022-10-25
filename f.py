from datetime import datetime

# d

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
    
    #e metode som returnerer en streng som kan skrives

    def __str__(self):
        #return Avtale  +str(self.tittel)+'/'+str(self.sted)+'/' """datetime eller int? """+datetime(self.starttidspunkt)+':'+int(self.varighet)
        return f"Tittel: {self.tittel}, Varighet: {self.varighet}"
#f
def lag_avtale():
    tittel = input("Skriv inn hva avtalen gjelder ")
    sted = str(input("Skriv sted "))
    starttidspunkt = input("Skriv starttidspunkt ")

    #datetime eller int?

    starttidspunkt = int(starttidspunkt)
    varighet = int(input("Skriv varighet på avtalen "))
    DinAvtale = Avtale(tittel, sted, starttidspunkt, varighet)
    return DinAvtale



