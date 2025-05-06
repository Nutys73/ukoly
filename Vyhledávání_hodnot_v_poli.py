cisla = []

for i in range(6):
    cislo = int(input(f"Zadejte číslo {i + 1}: "))
    cisla.append(cislo)
hledani = int(input("Zadejte číslo, které chcete najít: "))

nalezeno = False

for i in range(len(cisla)):
    if cisla[i] == hledani:
        print(f"Našel jsem tuto hodnotu na pozici {i}")
        nalezeno = True

        break  

if not nalezeno:
    print("Zadaná hodnota tady není.")
