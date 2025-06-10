from data import zvirata
def pridej_zvire(seznam, jmeno, druh):
    seznam.append((jmeno, druh))
def vypis_zvirata(seznam):
    for i, (jmeno, druh) in enumerate(seznam, start=1):
            print("f{i}. {jmeno} {druh}")
