from utulek import prijmoutZvire
from nemocnice import vypisPacienty
from radnice import pozdravitObcana
 
def menu():
    while True:
        print("\n--- Správa města ---")
        print("1. Přijmout zvíře do útulku")
        print("2. Vypsat pacienty v nemocnici")
        print("3. Pozdravit občana")
        print("0. Konec")
 
        volba = input("Zadej volbu: ")
        if volba == "1":
            jmeno = input("Zadej jmeno zvirete: ")
            prijmoutZvire(jmeno)
        elif volba == "2":
            vypisPacienty()
        elif volba == "3":
            jmeno = input("Zadej jmeno obcana: ")
            pozdravitObcana(jmeno)
        elif volba == "0":
            print("Ukoncuji program")
            break
        else:
            print("Neplatná volba")
 
menu()
