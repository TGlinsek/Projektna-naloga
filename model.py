# Navdih:
# https://www.khanacademy.org/computer-programming/box-it/5185240348000256
# https://www.mathsisfun.com/games/boxup-puzzle.html


class VsiLeveli:  # v vrstnem redu - ampak ne vsi, kr lah mamo tut custom level. Torej bomo imeli slovar
    
    def __init__(self, datoteka_z_leveli):
        self.datoteka_z_leveli = datoteka_z_leveli
        # oblika: {"0": matrika, "1": ..., "custom_level": ...}

        self.število_levelov = max([int(ključ) for ključ in self.datoteka_z_leveli.keys() if ključ.isdigit()])  # vsi ključi bodo stringi

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

        self.velikost_igralca = 0  # velikost je odvisna od tega, koliko škatel ima igralec okoli


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
        
        zadnji znak v nizu nikoli ne more biti pomišljaj ("-")
        """
    def preveri_okolico(self, nasprotna_smer):  # vrne True, kadar se lahko premakne v to smer
        polje_z_igralcem = self.matrika[self.koord_igralca[1], self.koord_igralca[0]]  # člen matrike, kjer je igralec
        koord_od_drugega_polja = None
        if nasprotna_smer == "v":  # gremo v levo
            koord_od_drugega_polja = (self.koord_igralca[0] - 1, self.koord_igralca[1])
        elif nasprotna_smer == "z":
            koord_od_drugega_polja = (self.koord_igralca[0] + 1, self.koord_igralca[1])
        elif nasprotna_smer == "j":
            koord_od_drugega_polja = (self.koord_igralca[0], self.koord_igralca[1] - 1)
        elif nasprotna_smer == "s":
            koord_od_drugega_polja = (self.koord_igralca[0], self.koord_igralca[1] + 1)
        drugo_polje = self.matrika[koord_od_levega_polja[1]][koord_od_levega_polja[0]]  # levo, desno, gornje ...
        
        nabor = (polje_z_igralcem, drugo_polje, koord_od_drugega_polja)
        
        if drugo_polje == "!":
            return False  # skala

        for znak in drugo_polje:
            if znak != nasprotna_smer and znak != "-":  # če je kaka škatla v napačno smer obrnjena
                return False  # ne more se igralec premakniti v to smer
        
        # preveriti moramo še notranjo velikost škatle:
        notranja_velikost_drugega_polja = 1  # to je najmanjša možna škatla. Igralčeva velikost je 0, zato še ravno lahko gre v to škatlo
        for znak in drugo_polje:
            if znak == "-":
                notranja_velikost_drugega_polja += 1
            else:
                break
        else:
            notranja_velikost_drugega_polja = float("inf")  # če drugo polje prazno polje

        # notranja in zunanja velikost posamezne škatle je vedno ista. Če pa imamo več škatel (eno v drugi), potem pa to ni več res in je zunanja velikost večja
        # velikost igralca meri zunanjo velikost (notranja je irelevantna oz. je ni)
        if notranja_velikost_drugega_polja > self.velikost_igralca:  # če paše not
            zunanja_velikost_drugega_polja = len(drugo_polje)

            # self.velikost_igralca = zunanja_velikost_drugega_polja  # to je samo za škatle. Če upoštevamo še prazna polja, moramo uporabiti spodnjo vrstico:
            self.velikost_igralca = max(zunanja_velikost_drugega_polja, self.velikost_igralca)  # to je zato, ker ima prazno polje zunanjo velikost 0 
            
            return nabor  # to je namesto True
        else:
            return False

    def premik_v_levo(self):  # to bo uredilo matriko self.matrika
        if self.koord_igralca[0] == 0:
            return False  # False vrnemo, če ni spremembe, True pa, če je
        
        okolica = preveri_okolico("v")  # tudi barvne škatle so notri vključene
        if okolica:  # če ni False
            igralec = okolica[0]
            polje = okolica[1]

            """
            Ustvarili bomo novo polje z naslednjo operacijo:

            "" + "" = ""
            "v" + "" = "v"  # operacija je tudi komutativna
            "vz" + "--j" = "vzj"
            "-j" + "-z" ne gre
            "-s" + "--j" = "-sj"
            """

            novo_polje = ""
            for par in itertools.zip_longest(igralec, polje, fillvalue="-"):
                novo_polje += par[0] if par[1] == "-" else par[1]
            
            print("Novo polje: " + novo_polje)
            koord_drugega_polja = okolica[2]
            self.matrika[koord_od_levega_polja[1]][koord_od_levega_polja[0]] = novo_polje  # posodobimo polje, kamor se je premaknil igralec
            self.matrika[self.koord_igralca[1], self.koord_igralca[0]] = ""  # izpraznimo polje, kjer je bil igralec
            self.koord_igralca = koord_drugega_polja  # posodobimo koordinate



    # za vsako polje v matriki lahko definiramo največjo velikost igralca (v kok vlki škatli je lahk), da še lahk gre na tisto polje. Če je prazno polje, je največja velikost neomejena
    # igralec po premiku dobi novo velikost, ki ni nujno ista kot ravnokar definirana količina. Dobimo jo pač s primerjavo členov matrike

    def preveri_ali_na_cilju(self):
        return vsi_elementi_seznama_so_isti(self.koord_barvnih_škatel)  # pri naborih nam ni treba skrbet za kazalce
    



