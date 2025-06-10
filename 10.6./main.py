import data
from evidence import pridej_zvire, vypis_zvirata

def menu():
    while True:
        print("\nVeterinarni centrum")
        print("1- Přidat zvíře")
        print("2- vypsat všechna zvířata")
        print("3- Ukončit")

        volba=input("Zadej volbu: ")
        if volba=="1":
            jmeno=input("Zadej jméno zvířete: ")
            druh=input("Zadej druh zvířete: ")
            pridej_zvire(data.zvirata, jmeno, druh)
        elif volba=="2":
            vypis_zvirata(data.zvirata)
        elif volba=="3":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba, zkus to znovu.")
menu()
