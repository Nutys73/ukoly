def pozdrav():
    print("Ahoj, jak se máš?")
 
def dnesni_den():
    dnes = datetime.datetime.now().strftime("%A")
    print(f"Dnes je {dnes}.")
 
def vypis_cisla():
    for i in range(1, 6):
        print(i)
 
def obdelnik():
    for _ in range(3):
        print("*" * 5)
 
def nalada_dne():
    nalady = ["veselá", "smutná", "unavená", "energická", "líná"]
    vybrana_nalada = random.choice(nalady)
    print(f"Dnešní nálada je: {vybrana_nalada}.")
 
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Pozdrav")
        print("2. Dnešní den")
        print("3. Čísla 1 až 5")
        print("4. Obdélník z hvězdiček")
        print("5. Nálada dne")
        print("6. Konec")
 
        volba = input("Zadej číslo: ")
 
        if volba == "1":
            pozdrav()
        elif volba == "2":
            dnesni_den()
        elif volba == "3":
            vypis_cisla()
        elif volba == "4":
            obdelnik()
        elif volba == "5":
            nalada_dne()
        elif volba == "6":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkus to znovu.")
 
menu()
