#ukol 1
def nasobek(cislo):
    vysledek=cislo*5
    print(vysledek)
nasobek(int(input("Zadejte číslo: ")))

#ukol 2
def vypisPrvniPole(pole):
    if len(pole)>0:
        print(pole[0])
    else:
        print("Pole je prázdné")
vypisPrvniPole([5,8,3])

#ukol 3

#ukol 4
def fiktivniPostava(jmeno, popis, věk):
    print(jmeno, popis, věk)
fiktivniPostava(input("Zadejte jméno postavy: "),input("Zadejte popis postavy: "),int(input("Zadejte vek postavy: ")))
