# Navdih:
# https://www.khanacademy.org/computer-programming/box-it/5185240348000256
# https://www.mathsisfun.com/games/boxup-puzzle.html

import itertools


def vsi_elementi_seznama_so_isti(seznam):  # pomožna funkcija
    if len(seznam) == 0:
        return True
    prvi_clen = seznam[0]
    for i in seznam[1:]:
        if i != prvi_clen:
            return False
    return True


class Koordinate:

    def __init__(self, nabor=None, zgornja_meja_x=float("inf"), zgornja_meja_y=float("inf")):  # zgornja meja ni vključena v možne koordinate
        if nabor is None:
            self.x = None
            self.y = None
        else:
            self.x, self.y = nabor
        self.zgornja_meja_x = zgornja_meja_x
        self.zgornja_meja_y = zgornja_meja_y 
    
    def nastavi_x(self, x):
        if self.zgornja_meja_x <= x:
            x = self.zgornja_meja_x - 1
        if x < 0:
            x = 0
        self.x = x
    
    def nastavi_y(self, y):
        if self.zgornja_meja_y <= y:
            y = self.zgornja_meja_y - 1
        if y < 0:
            y = 0
        self.y = y

    def spremeni_x_za(self, offset):
        self.nastavi_x(self.x + offset)
    
    def spremeni_y_za(self, offset):
        self.nastavi_y(self.y + offset)
    
    def kopiraj_koordinate_od_drugega(self, druge_koordinate):
        self.nastavi_x(druge_koordinate.x)
        self.nastavi_y(druge_koordinate.y)
    
    def kopiraj_svoje_koordinate(self):  # če napišemo samo return self, ne deluje pravilno
        nove_koord = Koordinate()  # zaenkrat sta koordinati še None
        nove_koord.kopiraj_koordinate_od_drugega(self)  # to naredimo zato, da objekta ne kažeta na isto stvar v pomnilniku
        return nove_koord

    def vrni_levega_soseda(self):
        nove_koord = self.kopiraj_svoje_koordinate() 
        nove_koord.spremeni_x_za(-1)
        return nove_koord
    
    def vrni_desnega_soseda(self):
        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_x_za(1)
        return nove_koord

    def vrni_zgornjega_soseda(self):  # višje vrstice imajo manjšo y-koordinato, kot pri matrikah (ne kot pri kartezičnem koordinatnem sistemu)
        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_y_za(-1)
        return nove_koord

    def vrni_spodnjega_soseda(self):  # višje vrstice imajo manjšo y-koordinato, kot pri matrikah (ne kot pri kartezičnem koordinatnem sistemu)
        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_y_za(1)
        return nove_koord
    
    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, drugo):   # to rabimo, ker zgleda da da če daš "==" vmes, potem gleda ali sta to en in isti objekt, zato vrne False, tudi če predstavljata objekta iste koordinate
        return self.x == drugo.x and self.y == drugo.y


class Matrika:

    def __init__(self, seznam_seznamov):  # notranji seznami so vrstice
        self.seznam_seznamov = seznam_seznamov  # vsi seznami so enako dolgi
        self.širina = len(self.seznam_seznamov[0])
        self.višina = len(self.seznam_seznamov)
    
    def preberi_člen(self, koord):
        return self.seznam_seznamov[koord.y][koord.x]
    
    def zamenjaj_člen(self, koord, člen):
        self.seznam_seznamov[koord.y][koord.x] = člen
    
    def kopiraj_sebe(self):
        nov_seznam = []
        for sez in self.seznam_seznamov:
            nov_seznam.append([])
            for i in sez:  # tukaj gremo vsak element posebej kopirati. Če kopiramo le sezname, ne deluje (ne vem še, zakaj točno ne). Drugače se tudi original spremeni, ko spremenimo kopijo.
                nov_seznam[-1].append(i)
        return Matrika(nov_seznam)

    def upodobitev(self):  # predstava, predstavitev, (re)prezentacija
        string = "┌"
        string += (2 * self.širina + 1) * " "
        string += "┐\n"
        for sez in self.seznam_seznamov:
            string += "│ "
            string += " ".join(("-" if element == "" else element) for element in sez)  # k sreči so členi matrike vsi nizi
            string += " │"
            string += "\n"
        string += "└"
        string += (2 * self.širina + 1) * " "
        string += "┘"
        return string
    
    def __repr__(self):
        return self.upodobitev()
    
    __str__ = __repr__


nasprotne_smeri = {"s": "j", "j": "s", "v": "z", "z": "v"}

def razberi(niz):
    if niz == "":
        return False
    znak = niz[-1]
    if znak == "-":  # pomišljaj ne bi smel biti na koncu
        return False
    if niz[:-1] == (len(niz) - 1) * "-":  # ta zadnji znak bi moral biti edini znak v nizu, ki ni pomišljaj
        return (znak, len(niz))
    else:
        return False
    

def razdeli(niz, smer):
    if niz == "":
        return ("", "")
    meja = 0
    for indeks_od_zadaj, znak in enumerate(niz[::-1]):
        if znak == smer or znak == "-":
            meja += 1
            continue
        break
    pomišljajev_v_ostanku = len(niz) - meja  # to niso nujno vsi pomišljaji
    prenos = niz[:pomišljajev_v_ostanku]
    
    if meja == 0:
        ostanek = ""  # lahko pa bi tudi samo spremenili pomišljajev_v_ostanku v 0. To je samo posledica našega formata.
    else:
        ostanek = pomišljajev_v_ostanku * "-" + niz[pomišljajev_v_ostanku:]
    return (ostanek, prenos)


def združi(prvi_člen, drugi_člen):
    vsota = ""
    for par in itertools.zip_longest(prvi_člen, drugi_člen, fillvalue="-"):
        vsota += par[0] if par[1] == "-" else par[1]
    return vsota


def povečaj(niz, indeks):  # kapitalizira indeksti znak v nizu
    return niz[:indeks] + niz[indeks].upper() + niz[indeks + 1:]


class Nivo:  # dejansko matrika, ki se spreminja

    # vsi členi seznama koord_barvnih_škatel bodo razredi Koordinate
    def __init__(self, seznam_seznamov, začetni_koord, seznam_naborov_barvnih_škatel):  # leveli bodo vedno taki (tudi v level editorju ne boš mogel narediti tako), da so škatle na začetku posebej (ni dveh skupaj)
        self.matrika = Matrika(seznam_seznamov)  # se spreminja
        self.koord_igralca = Koordinate(začetni_koord)  # nabor (x, y) (nikoli ne bomo spreminjali vsako koordinato posebej, ampak vsakič obe naenkrat. Torej lahko uporabimo nabor)
        seznam_objektov_barvnih_škatel = []
        for nabor in seznam_naborov_barvnih_škatel:
            seznam_objektov_barvnih_škatel.append(Koordinate(nabor))  # nabore koordinat bomo spreminjali v objekt Koordinate

        # koord_barvnih_škatel  # seznam naborov (po defaultu dveh, lahko več, ne more pa bit manj kot dve)

        # od leve proti desni naraščajo velikosti
        # posodobljen format (za barvne škatle): vključili bomo še usmerjenost in velikost škatel: [seznam_koordinat, seznam_usmerjenosti, seznam_velikosti]
        # na začetku je le seznam_koordinat: tule bomo pa še dodali usmerjentosti in velikosti, ki jih preberemo iz matrike
        # v bistvu, ne bomo naredili seznama, ampak raje slovar. Vsaka velikost se pojavi največ enkrat.

        # {"1": [(x, y), usmerjenost], "2": ...} takole bo slovar izgledal
        # zdaj bomo uporabili seznam naborov koord_barvnih škatel, da ustvarimo seznam. Pomagali si bomo s self.matrika:
        # predpostavili bomo, da na začetku v matriki ni "vgnezdenih" škatel
        """
        Potrebujemo funkcijo, ki:
        - spremeni "--s" v ("s", 3)
        - spremeni "j" v ("j", 1)
        - za "" vrne error
        - če je v nizu črk več kot ena, potem prav tako vrne error

        To bo naredila funkcija razberi().
        """
        slovar = {}
        for par_koordinat in seznam_objektov_barvnih_škatel:  # vrstni red v seznamu "koord_barvnih_škatel" ni pomemben. V vsakem primeru pride (oz. bi moral priti) isti rezultat
            člen_matrike = self.matrika.preberi_člen(par_koordinat)
            smer, velikost = razberi(člen_matrike)
            if smer not in ["s", "j", "v", "z"]:
                raise ValueError("Smer ni ustrezna")
            if type(velikost) == int:
                if velikost <= 0:
                    raise ValueError("Velikost ni pozitivna!")
            else:
                raise ValueError("Velikost ni (celo) število!")
            if slovar.get(velikost, None) is None:  # če na tem naslovu v slovarju še ni ničesar 
                slovar[str(velikost)] = [par_koordinat, smer]
            else:
                raise ValueError("Ta velikost je že zasedena. Vse velikosti barvnih škatel morajo biti različne!")
        self.slovar_barvnih_škatel = slovar
        # morda lahko podatek o smeri odstranimo iz slovarja. Zaenkrat naj ostane notri

        self.velikost_igralca = 0  # velikost je odvisna od tega, koliko škatel ima igralec na svojem polju


        # barvne škatle so še vseeno shranjene v matriki, zato da poznamo usmerjenost
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
    
    def dodaj_barvno_škatlo(self, velikost, koordinate):  # za level editor. Default smer je sever. Kasneje lahko še rotiramo
        pass

    def odstrani_barvno_škatlo(self, velikost):
        pass
    
    def rotiraj_škatlo(self, koordinate, smer):  # smer je tukaj lahko ali v smeri urinega kazalca ali pa proti. "+" bo v smeri proti, "-" v nasprotni.
        pass

    # tole je namenjeno le za prikaz igralcu:
    def matrika_z_igralcem(self):  # in tudi s poudarjenimi barvnimi škatlami
        kopija = self.matrika.kopiraj_sebe()
        for ključ in self.slovar_barvnih_škatel:  # za upodobitev položajev barvnih škatel. Kapitalizirane črke pomenijo barvne škatle
            koord = self.slovar_barvnih_škatel[ključ][0]
            kopija.zamenjaj_člen(koord, povečaj(kopija.preberi_člen(koord), int(ključ) - 1))
        kopija.zamenjaj_člen(self.koord_igralca, kopija.preberi_člen(self.koord_igralca) + "+")  # "+" bo označeval igralca
        return kopija

    def __str__(self):
        return str(self.matrika_z_igralcem())
    
    __repr__ = __str__

    def preveri_okolico(self, smer):  # vrne True, kadar se lahko premakne v to smer
        nasprotna_smer = nasprotne_smeri[smer]
        polje_z_igralcem = self.matrika.preberi_člen(self.koord_igralca)  # člen matrike, kjer je igralec
        koord_od_drugega_polja = None
        if nasprotna_smer == "v":  # gremo v levo
            koord_od_drugega_polja = self.koord_igralca.vrni_levega_soseda()
        elif nasprotna_smer == "z":
            koord_od_drugega_polja = self.koord_igralca.vrni_desnega_soseda()
        elif nasprotna_smer == "j":  # gremo gor
            koord_od_drugega_polja = self.koord_igralca.vrni_zgornjega_soseda()
        elif nasprotna_smer == "s":
            koord_od_drugega_polja = self.koord_igralca.vrni_spodnjega_soseda()
        drugo_polje = self.matrika.preberi_člen(koord_od_drugega_polja)  # levo, desno, gornje ...
        
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

        # ampak najprej bomo razdelili igralčevo polje na ostanek in prenos:
        """
        Razdelili bomo igralčevo polje na del, ki se loči, in del, ki ostane. Operacija bo odvisna od smeri.

        "sjz" v smeri zahoda: "--z" ostane, "sj" gre stran
        "szz" v smeri zahoda: "-zz" ostane, "s" gre stran
        "zzz" v smeri zahoda: "zzz" ostane, "" gre stran
        "sjs" v smeri zahoda: "" ostane, "sjs" gre stran (ne loči se)
        "szs" ali "zzs" v smeri zahoda: ne loči se, oz., ostane "", vse gre stran
        "": ostane "", stran gre "".
        "z" v smeri z: ostane "z", prenos ""
        "s" v smeri z: ostane "", prenos "s"
        "z-z" v smeri z: ostane "z-z", prenos ""
        "zs-z" v smeri z: ostane "---z", gre "zs"
        "z-sz" v smeri z: ostane "---z", gre "z-s"
        "z-s-z-j-z" v smeri z: ostane "--------z", gre "z-s-z-j"

        To operacijo bomo opisali v funkciji razdeli()
        """

        ostanek, prenos = razdeli(polje_z_igralcem, smer)  # sprejme prvotni člen in pa smer ter vrne nabor (ostane, gre stran)
        
        zunanja_velikost_prenosa = len(prenos)  # dejansko igralca (štejemo le škatle, ki grejo z njim)
        if notranja_velikost_drugega_polja > zunanja_velikost_prenosa:  # če paše not

            # če so koordinate barvnih škatel iste kot koordinate igralca, potem poglej, ali so barvne škatle v ostanku ali prenosu (saj v tem primeru v polju mora biti prava usmerjenost na pravem mestu, saj poznamo velikost škatel)
            # če je v ostanku, se nič ne spremeni. Če v prenosu, pa se.
            barvne_škatle_se_premaknejo = {}
            for ključ in self.slovar_barvnih_škatel:
                if self.slovar_barvnih_škatel[ključ][0] == self.koord_igralca:  # če so barvne škatle na istem mestu kot igralec
                    velikost = int(ključ)  # velikost barvne škatle je kar ključ
                    if len(prenos) >= velikost:
                        barvne_škatle_se_premaknejo[ključ] = True
                    else:
                        barvne_škatle_se_premaknejo[ključ] = False
                else:
                    barvne_škatle_se_premaknejo[ključ] = False

            nabor = (ostanek, prenos, drugo_polje, koord_od_drugega_polja, barvne_škatle_se_premaknejo)  # [True, False, False, ...] po vrsti barvne škatle
            # v bistvu bo to slovar: {"1": True, "2": False, ...}, ne seznam


            zunanja_velikost_drugega_polja = len(drugo_polje)

            # self.velikost_igralca = zunanja_velikost_drugega_polja  # to je samo za škatle. Če upoštevamo še prazna polja, moramo uporabiti spodnjo vrstico:
            self.velikost_igralca = max(zunanja_velikost_drugega_polja, zunanja_velikost_prenosa)  # to je zato, ker ima prazno polje zunanjo velikost 0 
            # zunanja velikost se ne spremeni, če gremo na prazno polje

            return nabor  # to je namesto True
        else:
            return False

    def premik_v_smer(self, smer):  # to bo uredilo matriko self.matrika
        # leva smer pomeni smer "z"
        if smer == "z":
            if self.koord_igralca.x == 0:
                return False  # False vrnemo, če ni spremembe, True pa, če je
        if smer == "v":
            if self.koord_igralca.x == self.matrika.širina - 1:
                return False
        if smer == "s":
            if self.koord_igralca.y == 0:
                return False
        if smer == "j":
            if self.koord_igralca.y == self.matrika.višina - 1:
                return False
        
        okolica = self.preveri_okolico(smer)  # tudi barvne škatle so notri vključene
        if okolica:  # če ni False
            ostanek, prenos, polje, koord_drugega_polja, b_škatle = okolica
            """
            Ustvarili bomo novo polje z naslednjo operacijo:

            "" + "" = ""
            "v" + "" = "v"  # operacija je tudi komutativna
            "vz" + "--j" = "vzj"
            "-j" + "-z" ne gre
            "-s" + "--j" = "-sj"

            To operacijo bomo opisali v funkciji združi()
            """
            
            novo_polje = združi(prenos, polje)

            self.matrika.zamenjaj_člen(koord_drugega_polja, novo_polje)  # posodobimo polje, kamor se je premaknil igralec
            self.matrika.zamenjaj_člen(self.koord_igralca, ostanek)  # izpraznimo polje, kjer je bil igralec, razen če imamo ostanek
            self.koord_igralca.kopiraj_koordinate_od_drugega(koord_drugega_polja)  # posodobimo koordinate
            
            # tukaj posodobimo še morebitne koordinate barvnih škatel
            for ključ in b_škatle:
                if b_škatle[ključ] == True:
                    self.slovar_barvnih_škatel[ključ][0].kopiraj_koordinate_od_drugega(koord_drugega_polja)
            return True
        return False

    # za vsako polje v matriki lahko definiramo največjo velikost igralca (v kok vlki škatli je lahk), da še lahk gre na tisto polje. Če je prazno polje, je največja velikost neomejena
    # igralec po premiku dobi novo velikost, ki ni nujno ista kot ravnokar definirana količina. Dobimo jo pač s primerjavo členov matrike

    def preveri_ali_na_cilju(self):
        return vsi_elementi_seznama_so_isti([self.slovar_barvnih_škatel[ključ][0] for ključ in self.slovar_barvnih_škatel.keys()])  # pri naborih nam ni treba skrbet za kazalce


class VsiNivoji:  # v vrstnem redu - ampak ne vsi, kr lah mamo tut custom level. Torej bomo imeli slovar
    
    def __init__(self, datoteka_z_nivoji):
        self.datoteka_z_nivoji = datoteka_z_nivoji
        # oblika: {"0": matrika, "1": ..., "custom_level": ...}

        self.število_nivojev = max([int(ključ) for ključ in self.datoteka_z_nivoji.keys() if ključ.isdigit()])  # vsi ključi bodo stringi

    def naslednji_nivo(self, id_trenutnega_nivoja):
        if type(id_trenutnega_nivoja) is int:
            if 0 <= id_trenutnega_nivoja < self.število_nivojev:
                return id_trenutnega_nivoja + 1
            elif id_trenutnega_nivoja == self.število_nivojev:
                return None  # to je bil zadnji level
        else:
            return None  # custom leveli niso razporejeni po vrsti


def vrni_prazen_nivo(širina, višina):  # imel bo igralca v levem zgornjem kotu, potem pa dve barvni škatli: manjšo desno zgoraj, večjo desno spodaj
    seznam_seznamov = []
    for i in range(višina):
        seznam_seznamov.append([])
        for j in range(širina):
            seznam_seznamov[-1].append("")
    seznam_seznamov[0][širina - 1] = "s"
    seznam_seznamov[višina - 1][širina - 1] = "-s"
    return Nivo(seznam_seznamov, Koordinate(0, 0), [Koordinate(širina - 1, 0), Koordinate(širina - 1, višina - 1)])

            
class UrejevalnikNivojev:  # level editor

    # None v primeru da začnemo nov nivo od začetka
    def __init__(self, trenutni_nivo=None, ime=None, širina=None, višina=None):  # klicalo se bo tako: UrejevalnikNivojev(VsiNivoji[ključ], ključ)
        if trenutni_nivo is None:
            self.trenutni_nivo = vrni_prazen_nivo(širina, višina)
        else:
            self.trenutni_nivo = trenutni_nivo  # Level
            self.ime = ime
    
    def izrisi(self):
        pass

    def dodaj_element(self, element, polje):  # element je nek niz, kot smo imeli pri nivojih. Dva elementa ne moreta biti na istem mestu na začetku.
        pass
    # element se izbriše tako, da dodaš na tisto mesto prazen string

    
    def izbrisi_vse(self):  # resetira nivo
        self.trenutni_nivo = vrni_prazen_nivo(self.trenutni_nivo.matrika.širina, self.trenutni_nivo.matrika.višina)  # vzame kar iste dimenzije kot so bile pred izbrisom
    
    
    def dodaj_level(self):
        # dodamo nov level v seznam VsiNivoji, pod novim imenom
        pass

    # ko submitaš level, ni poti nazaj in je vsem viden.

    def rotiraj(self, koordinate):
        pass











