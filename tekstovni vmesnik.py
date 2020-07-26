# samo za testiranje delovanja modela
from model import Level

def zahtevaj_smer():
    smer = input("Prestavi igralca! (možnosti: s, j, v, z)")
    return smer.lower()

def izpis_zmage():
    print("Zmaga!")

def izpis_položaja(igra):
    print(igra)  # ker imamo __str__

def pozeni_tekstovni_vmesnik():

    # nek poljuben level:
    igra = Level([["", "", ""], ["", "z", ""], ["", "", "-s"]], (0, 0), [(2, 2), (1, 1)])  # dejansko koordinate niso nujno v vrstnem redu, kjer bi škatle naraščale po velikosti. Lahko poskrbimo tudi za to!
    while True:
        izpis_položaja(igra)
        if igra.preveri_ali_na_cilju():
            izpis_zmage()
            break
        smer = zahtevaj_smer()
        igra.premik_v_smer(smer)
    return

