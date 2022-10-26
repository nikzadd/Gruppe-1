from g import avtaler
def avtale_til_tekstfil(avtalefil):
    for linje in avtaler():
        avtalefil.write(linje + "\n")
avtalefil = open("avatalefil.txt", "w", encoding="UTF8")

