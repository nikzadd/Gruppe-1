from g import avtaler
def avtale_til_tekstfil(avtaler):
    for linje in avtaler:
        avtale_til_tekstfil.write(str((i+1, avtaler[linje].tittel, avtaler[linje].sted,
            avtaler[linje].varighet, avtaler[linje].starttidspunkt + "\n"))
avtalefil = open("avatalefil.txt", "w", encoding="UTF8")
