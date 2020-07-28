# samo za testiranje delovanja modela
# from model import Level
from model import Nivo


def zahtevaj_smer():
    smer = input("Prestavi igralca! (možnosti: s, j, v, z)")
    return smer.lower()


def izpis_zmage():
    print("Zmaga!")


def izpis_položaja(igra):
    print(igra)  # ker imamo __str__
    print("Koordinate igralca: " + str(igra.koord_igralca))


def pozeni_tekstovni_vmesnik():
    # nek poljuben level:
    igra = Nivo([["", "", ""], ["", "z", ""], ["", "", "-s"]], (0, 0), [(2, 2), (1, 1)])  # dejansko koordinate niso nujno v vrstnem redu, kjer bi škatle naraščale po velikosti. Navsezadnje bodo vpisane v slovar.
    # ti nivoji bodo na koncu vsi shranjeni v objektu VsiNivoji, ali kaj podobnega
    while True:
        izpis_položaja(igra)
        if igra.preveri_ali_na_cilju():
            izpis_zmage()
            break
        smer = zahtevaj_smer()
        igra.premik_v_smer(smer)
    return

pozeni_tekstovni_vmesnik()