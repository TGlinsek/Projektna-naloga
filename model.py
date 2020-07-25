# Navdih:
# https://www.khanacademy.org/computer-programming/box-it/5185240348000256
# https://www.mathsisfun.com/games/boxup-puzzle.html


class VsiLeveli:  # v vrstnem redu - ampak ne vsi, kr lah mamo tut custom level. Torej bomo imeli slovar
    
    def __init__(self, datoteka_z_leveli):
        self.datoteka_z_leveli = datoteka_z_leveli
        # oblika: {"0": matrika, "1": ..., "custom_level": ...}

        self.število_levelov = max([for ključ in self.datoteka_z_leveli.keys() if type(ključ) is int])

    def naslednji_level(self, trenutni_level_id):
        if type(trenutni_level_id) is int:
            if 0 <= trenutni_level_id < self.število_levelov:
                return trenutni_level_id + 1
            elif trenutni_level_id == self.število_levelov:
                return None  # to je bil zadnji level
        else:
            return None  # custom leveli niso razporejeni po vrsti


def vsi_elementi_seznama_so_isti(seznam):  # pomožna funkcija
    if len(seznam) == 0:
        return True
    prvi_clen = seznam[0]
    for i in seznam[1:]:
        if i != prvi_clen:
            return False
    return True


class Level:  # dejansko matrika, ki se spreminja

    def __init__(self, matrika, začetni_koord, koord_barvnih_škatel):
        self.matrika = matrika  # se spreminja
        self.koord_igralca = začetni_koord  # nabor (x, y)
        self.koord_barvnih_škatel = koord_barvnih_škatel  # seznam naborov (po defaultu dveh, ne more pa bit manj kot dve)
        # od leve proti desni naraščajo velikosti


        # barvne škatle so še vseeno shranjene v matriki, zato da vemo usmerjenost
        """
        matrika izgleda tako:
        ┌       ┐
        │ 2 3 4 │
        │ 1 1 0 │
        │ 0 1 3 │
        └       ┘
        v pythonu pa je identiteta recimo [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        sam da niso not številke, ampak stringi:

        # "" je prazno polje
        # "-sz" 3 chari so lah sam če mamo tri nivoje, kar pa ni v izvornih igrah
        # "sj"
        # "-v"
        # "-g"
        # "d"
        # "v"
        # "!" skala

        na prvem mestu je manjša škatla, na drugem večja (minus damo uspred), vlkih črk ni več (mamo posebi spremenljivko za to)

        """
    
    def premik_v_levo(self):  # to bo uredilo matriko self.matrika
        if self.koord_igralca[0] == 0:
            return False  # False vrnemo, če ni spremembe, True pa, če je
        koord_od_levega_polja = (self.koord_igralca[0] - 1, self.koord_igralca[1])
        if preveri_okolico(self.koord_igralca, self.matrika[koord_od_levega_polja[1]][koord_od_levega_polja[0]]):  # tudi barvne škatle so notri vključene
            pass
    
    # za vsako polje v matriki lahko definiramo največjo velikost igralca (v kok vlki škatli je lahk), da še lahk gre na tisto polje. Če je prazno polje, je največja velikost neomejena
    # igralec po premiku dobi novo velikost, ki ni nujno ista kot ravnokar definirana količina. Dobimo jo pač s primerjavo členov matrike

    def preveri_če_na_cilju(self):
        return vsi_elementi_seznama_so_isti(self.koord_barvnih_škatel)  # pri naborih nam ni treba skrbet za kazalce
    



