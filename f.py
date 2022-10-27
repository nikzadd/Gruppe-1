# d

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
    
#e metode som returnerer en streng som kan skrives

    def __str__ (self):
        return f"Tittel: {self.tittel}, Sted: {self.sted}, StartTidspunkt: {self.starttidspunkt} Varighet: {self.varighet}"

#f

from datetime import datetime
def lag_avtale():
    tittel = input("Skriv inn hva avtalen gjelder: ")
    sted = str(input("Skriv sted: "))
    dato = input("Skriv inn starttidspunkt. Skriv på format: YYYY-MM-DD TT:MM:SS")
    starttidspunkt = datetime.fromisoformat(dato)
    varighet = int(input("Skriv varighet på avtalen: "))
    DinAvtale = Avtale(tittel, sted, starttidspunkt, varighet)
    return DinAvtale

if __name__ =="__main__":
<<<<<<< HEAD
    lag_avtale()
=======
    lag_avtale()


>>>>>>> f04859105f7d922ed5d9df1b01e76000333edbb0
