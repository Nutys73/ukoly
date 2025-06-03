#ukol1
import random
 
def hadani_Cisel(tajne_cislo):
    while True:
        tip = int(input("Zadej cislo(1-100): "))
        if tip < tajne_cislo:
            print("Hledane cislo je vyssi.")
        elif tip > tajne_cislo:
            print("Hledane cislo je nizsi")
        else:
            print("Spravne!!!")
            break
tajne_cislo = random.randint(1,100)
hadani_Cisel(tajne_cislo)
 
#ukol2
def pocet_znaku(text, znak):
    text = text.lower()
    znak = znak.lower()
    pocet = 0
    for pismeno in text:
        if pismeno == znak:
            pocet += 1
    return pocet
print(pocet_znaku("ahoj svete","e"))
 
#ukol3
def obrat_retezec(text):
    novy_text = " "
    for znak in text:
        novy_text = znak + novy_text
    return novy_text
print(obrat_retezec("Pythno"))
