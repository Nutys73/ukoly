# Načtení skóre hráčů
skore = []
print("Zadej skóre 10 hráčů (0 až 60):")
for i in range(10):
   bod = int(input(f"Hráč {i + 1}: "))
   skore.append(bod)
# Výpis všech skóre
print("\nSkóre hráčů:", skore)
# Výpočty
prumer = sum(skore) / 10
nejvyssi = max(skore)
nejnizsi = min(skore)
print("Průměrné skóre:", prumer)
print("Nejvyšší skóre:", nejvyssi)
print("Nejnižší skóre:", nejnizsi)
# Hodnocení výkonu
nad_50 = 0
for bod in skore:
   if bod > 50:
       nad_50 += 1
if nad_50 > 5:
   print("Výborný výkon!")
else:
   print("Můžete to příště zkusit lépe.")
