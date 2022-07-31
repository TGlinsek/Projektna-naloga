# Navdih:
# https://www.khanacademy.org/computer-programming/box-it/5185240348000256
# https://www.mathsisfun.com/games/boxup-puzzle.html

import itertools
import json
from copy import deepcopy

import os

from pathlib import Path


def pridobi_relativno_pot(ime):
    """
    Ime je npr. "uporabniki.json",
    funkcija pa vrne "UVP\\Projektna-naloga\\uporabniki.json", v primeru, 
    da imam vsc odprt v mapi, ki vsebuje mapo "UVP"
    """
    cwd = os.getcwd()
    prava_pot = os.path.realpath(__file__)
    starš = Path(prava_pot).parent
    relativna_pot = os.path.relpath(starš, start=cwd)
    return os.path.join(relativna_pot, ime)


def vsi_elementi_seznama_so_isti(seznam):
    """
    Pomožna funkcija, ki preveri, ali so vsi elementi 
    seznama enaki (z uporabo enačaja "==").
    
    Objekti razreda Koordinate so za to funkcijo enaki, 
    če imajo vsi enak atribut x in enak atribut y.
    V razredu smo namreč definirali metodo __eq__.
    """
    if len(seznam) == 0:
        return True
    prvi_clen = seznam[0]
    for i in seznam[1:]:
        if i != prvi_clen:
            return False
    return True


class Koordinate:

    def __init__(self, nabor=None, zgornja_meja_x=float("inf"), zgornja_meja_y=float("inf")):
        # zgornja meja ni vključena v možne koordinate

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

    def vrni_nabor(self):
        return self.x, self.y

    def spremeni_x_za(self, offset):
        self.nastavi_x(self.x + offset)

    def spremeni_y_za(self, offset):
        self.nastavi_y(self.y + offset)

    def kopiraj_koordinate_od_drugega(self, druge_koordinate):
        self.nastavi_x(druge_koordinate.x)
        self.nastavi_y(druge_koordinate.y)

    def kopiraj_svoje_koordinate(self):
        # če napišemo samo return self, ne deluje pravilno

        nove_koord = Koordinate()  # zaenkrat sta koordinati še None

        nove_koord.kopiraj_koordinate_od_drugega(self)
        # to naredimo zato, da objekta ne kažeta na isto stvar v pomnilniku

        return nove_koord

    def vrni_levega_soseda(self):
        # to bi verjetno lahko spravili v eno samo

        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_x_za(-1)
        return nove_koord

    def vrni_desnega_soseda(self):
        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_x_za(1)
        return nove_koord

    def vrni_zgornjega_soseda(self):
        # višje vrstice imajo manjšo y-koordinato, kot pri matrikah
        # (ne kot pri kartezičnem koordinatnem sistemu)

        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_y_za(-1)
        return nove_koord

    def vrni_spodnjega_soseda(self):
        # višje vrstice imajo manjšo y-koordinato, kot pri matrikah
        # (ne kot pri kartezičnem koordinatnem sistemu)

        nove_koord = self.kopiraj_svoje_koordinate()
        nove_koord.spremeni_y_za(1)
        return nove_koord

    def koordinate_gredo_v_matriko_dimenzij(self, širina, višina):
        return 0 <= self.x < širina and 0 <= self.y < višina

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, drugo):
        # to potrebujemo, saj izgleda da če daš "==" vmes,
        # potem koda gleda ali sta to en in isti objekt, zato vrne False,
        # tudi če predstavljata objekta iste koordinate

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
            for i in sez:
                # tukaj gremo vsak element posebej kopirati.
                # Če kopiramo le sezname, ne deluje
                # (saj so seznami shranjeni na istem mestu v pomnilniku).
                # Drugače se tudi original spremeni, ko spremenimo kopijo.
                nov_seznam[-1].append(i)
        return Matrika(nov_seznam)

    def upodobitev(self):
        string = "┌"
        string += (2 * self.širina + 1) * " "
        string += "┐\n"
        for sez in self.seznam_seznamov:
            string += "│ "
            string += " ".join(("-" if element == "" else element) for element in sez)
            string += " │"
            string += "\n"
        string += "└"
        string += (2 * self.širina + 1) * " "
        string += "┘"
        return string

    def __repr__(self):
        return self.upodobitev()

    __str__ = __repr__


znaki = ["a", "d", "w", "s"]


nasprotne_smeri = {znaki[2]: znaki[3], 
                   znaki[3]: znaki[2], 
                   znaki[1]: znaki[0], 
                   znaki[0]: znaki[1]}

# vrtenje v pozitivno smer
rotirane_smeri = {znaki[2]: znaki[0], 
                  znaki[0]: znaki[3], 
                  znaki[3]: znaki[1], 
                  znaki[1]: znaki[2]}


def razberi(niz):
    """
    - spremeni "--w" v ("w", 3)
    - spremeni "s" v ("s", 1)
    - za "" vrne error
    - če je v nizu črk več kot ena, potem prav tako vrne error
    """
    if niz == "":
        return False
    znak = niz[-1]
    if znak == "-":  # pomišljaj ne bi smel biti na koncu
        return False
    # ta zadnji znak bi moral biti edini znak v nizu, ki ni pomišljaj
    if niz[:-1] == (len(niz) - 1) * "-":
        return znak, len(niz)
    else:
        return False


def razdeli(niz, smer):
    """
    - "sjz" v smeri zahoda: "--z" ostane, "sj" gre stran
    - "szz" v smeri zahoda: "-zz" ostane, "s" gre stran
    - "zzz" v smeri zahoda: "zzz" ostane, "" gre stran
    - "sjs" v smeri zahoda: "" ostane, "sjs" gre stran (ne loči se)
    - "szs" ali "zzs" v smeri zahoda: ne loči se, oz., ostane "", vse gre stran
    - "": ostane "", stran gre "".
    - "z" v smeri z: ostane "z", prenos ""
    - "s" v smeri z: ostane "", prenos "s"
    - "z-z" v smeri z: ostane "z-z", prenos ""
    - "zs-z" v smeri z: ostane "---z", gre "zs"
    - "z-sz" v smeri z: ostane "---z", gre "z-s"
    - "z-s-z-j-z" v smeri z: ostane "--------z", gre "z-s-z-j"
    """
    if niz == "":
        return "", ""
    meja = 0
    for indeks_od_zadaj, znak in enumerate(niz[::-1]):
        if znak == smer or znak == "-":
            meja += 1
            continue
        break
    pomišljajev_v_ostanku = len(niz) - meja  # to niso nujno vsi pomišljaji
    prenos = niz[:pomišljajev_v_ostanku]

    if meja == 0:
        ostanek = ""  
        # lahko pa bi tudi samo spremenili pomišljajev_v_ostanku v 0
    else:
        ostanek = pomišljajev_v_ostanku * "-" + niz[pomišljajev_v_ostanku:]
    return ostanek, prenos


def združi(prvi_člen, drugi_člen):
    """
    - "" + "" = ""
    - "v" + "" = "v"
    - "vz" + "--j" = "vzj"
    - "-j" + "-z" ne gre
    - "-s" + "--j" = "-sj"
    """
    vsota = ""
    for par in itertools.zip_longest(prvi_člen, drugi_člen, fillvalue="-"):
        vsota += par[0] if par[1] == "-" else par[1]
    return vsota


def povečaj(niz, indeks):  
    """
    Kapitalizira znak v nizu, ki je na mestu številka "indeks"
    """
    return niz[:indeks] + niz[indeks].upper() + niz[indeks + 1:]


def škatla(velikost, smer):
    """ 
    vrne niz za posamezno škatlo. 
    Velikost 3 je npr. "--s"
    """
    return (velikost - 1) * "-" + smer.lower()


def je_škatla(člen):
    """
    Preveri, ali ta niz predstavlja škatlo
    """
    if člen == "":
        return False
    return člen[-1] in znaki and člen[:-1] == "-" * (len(člen) - 1)


class Nivo:  # matrika, ki se spreminja, z nekaj dodatnimi atributi

    # vsi členi seznama koord_barvnih_škatel bodo razreda Koordinate
    def __init__(self, seznam_seznamov, začetni_koord, seznam_naborov_barvnih_škatel):
        self.matrika = Matrika(seznam_seznamov)  # se spreminja
        self.koord_igralca = Koordinate(tuple(začetni_koord))
        # nabor (x, y) (nikoli ne bomo spreminjali vsako koordinato posebej,
        # ampak vsakič obe naenkrat. Torej lahko uporabimo nabor)

        # to je potrebno, saj nočemo pred vsakim naborom pisati besedo "Koordinate"

        self.velikostna_stopnja = len(max(max
                                          (seznam_seznamov, key=lambda v: len(max(v, key=len))), 
                                          key=len)
                                      )
        # vrne največjo velikost, ki se pojavi v nivoju

        self.št_potez = 0

        množica_objektov_barvnih_škatel = []

        # to bi sicer lahko bila množica, ampak json ne podpira množic
        for nabor in seznam_naborov_barvnih_škatel:
            # nabore koordinat bomo spreminjali v objekt Koordinate
            množica_objektov_barvnih_škatel.append(Koordinate(tuple(nabor)))

        # od leve proti desni naraščajo velikosti

        # posodobljen format (za barvne škatle): vključili bomo še
        # usmerjenost in velikost škatel: 
        # [seznam_koordinat, seznam_usmerjenosti, seznam_velikosti]

        # na začetku je le seznam_koordinat: tule bomo pa še
        # dodali usmerjentosti in velikosti, ki jih preberemo iz matrike

        # v bistvu, ne bomo naredili seznama, ampak raje slovar.
        # Vsaka velikost se namreč pojavi največ enkrat.

        # {"1": [(x, y), usmerjenost], "2": ...} takole bo slovar izgledal

        # zdaj bomo uporabili seznam naborov koord_barvnih škatel,
        # da ustvarimo seznam. Pomagali si bomo s self.matrika:

        # predpostavili bomo, da na začetku v matriki ni
        # "vgnezdenih" škatel (dveh škatel z istimi koordinatami)

        """
        Potrebujemo funkcijo, ki:
        - spremeni "--w" v ("w", 3)
        - spremeni "s" v ("s", 1)
        - za "" vrne error
        - če je v nizu črk več kot ena, potem prav tako vrne error

        To bo naredila funkcija razberi().
        """
        
        slovar = {}
        for par_koordinat in množica_objektov_barvnih_škatel:
            # vrstni red v seznamu "koord_barvnih_škatel" ni pomemben.
            # V vsakem primeru pride (oz. bi moral priti) isti rezultat

            člen_matrike = self.matrika.preberi_člen(par_koordinat)
            smer, velikost = razberi(člen_matrike)
            if smer not in znaki:
                raise ValueError("Smer ni ustrezna")
            if type(velikost) == int:
                if velikost <= 0:
                    raise ValueError("Velikost ni pozitivna!")
            else:
                raise ValueError("Velikost ni (celo) število!")
            if slovar.get(velikost, None) is None:  
                # če na tem naslovu v slovarju še ni ničesar:
                slovar[str(velikost)] = [par_koordinat, smer]
            else:
                raise ValueError("Ta velikost je že zasedena. "
                                 "Vse velikosti barvnih škatel morajo biti različne!")
        self.slovar_barvnih_škatel = slovar

        self.velikost_igralca = 0
        # velikost je odvisna od tega, koliko škatel ima igralec na svojem polju

        # barvne škatle so še vseeno shranjene v matriki, zato da poznamo usmerjenost
        """
        Možni členi matrike:

        # "" je prazno polje
        # "-wa" 3 chari so lah sam če mamo tri nivoje, kar pa ni v izvornih igrah
        # "ws"
        # "-d"
        # "-a"
        # "d"
        # "s"
        # "!" skala

        # črke pomenijo smer, kjer ima škatla luknjo. Škatle naraščajo od leve proti
        # desni, npr. v "aw" je škatla z luknjo na desni ("a") vsebovana
        # v škatli z luknjo zgoraj ("w")

        # "-" dodamo, če večja škatla ne vsebuje nobene manjše

        zadnji znak v nizu nikoli ne more biti pomišljaj ("-")
        """

    # za barvne škatle
    def pridobi_seznam_naborov(self):
        # to je zato, da ne shranjujemo nepotrebnih
        # informacij o smereh in velikosti barvnih škatel. Zanima nas le lokacija

        sez = []
        for ključ in self.slovar_barvnih_škatel:
            objekt_koord = self.slovar_barvnih_škatel[ključ][0]
            sez.append(objekt_koord.vrni_nabor())
        return sez
    # to se bo klicalo, ko bomo določeno stanje v levelu
    # (ali ko igramo, ali pa ko urejamo) vpisali v JSON

    def vrni_parametre(self):
        # vrne parametre za izdelavo levela
        # (to je nabor, v katerem je seznam seznamov, začetne
        # koordinate, in koordinate barvnih škatel)
        return (self.matrika.seznam_seznamov, 
                self.koord_igralca.vrni_nabor(), 
                self.pridobi_seznam_naborov())

    def dodaj_element(self, koordinate, člen):
        # za level editor. Default smer je sever. Kasneje lahko še rotiramo

        # še za igralca (zato matrika z igralcem)
        if self.matrika_z_igralcem().preberi_člen(koordinate) == "":
            self.matrika.zamenjaj_člen(koordinate, člen)
        else:
            return True
            # raise ValueError("Polje je že zasedeno!")

    def dodaj_škatlo(self, velikost, koordinate):
        return self.dodaj_element(koordinate, škatla(velikost, znaki[2]))
        # return je zato da sporočimo morebitno napako

    def dodaj_barvno_škatlo(self, velikost, koordinate):
        napaka = self.dodaj_škatlo(velikost, koordinate)
        if napaka:  # polje zasedeno
            return True
        # če barvno škatlo samo prestavljamo, ne pa dodajamo na novo
        if str(velikost) in self.slovar_barvnih_škatel.keys():
            stare_koord = self.slovar_barvnih_škatel[str(velikost)][0]

            # tu ne moremo dati odstrani_element, saj ga to zmede (misli, da bomo brisali barvno škatlo)
            self.matrika.zamenjaj_člen(stare_koord, "")
            # vzemi koordinate in zbriši škatlo na prejšnjem mestu (če te vrstice ni, ostane navadna škatla)
        self.slovar_barvnih_škatel[str(velikost)] = (koordinate, znaki[2])

    def odstrani_element(self, koordinate):
        if self.koord_igralca == koordinate:
            return 2
            # raise ValueError("Igralec mora vedno biti prisoten!")
        člen = self.matrika_z_igralcem().preberi_člen(koordinate)
        if člen == "":  # ker potem člen[-1] ne deluje
            return
        if člen[-1].lower() != člen[-1]:  # barvna škatla
            velikost = len(člen)
            if len(self.slovar_barvnih_škatel) == 2:  # 2 je najmanj
                return True
            else:
                self.odstrani_barvno_škatlo(velikost)
        self.matrika.zamenjaj_člen(koordinate, "")

    def odstrani_barvno_škatlo(self, velikost):
        # če odstranjuješ barvno škatlo, raje kliči odstrani_element
        self.slovar_barvnih_škatel.pop(str(velikost))
        # https://stackoverflow.com/questions/11277432/how-to-remove-a-key-from-a-python-dictionary

    def rotiraj_škatlo(self, koordinate, smer):
        # smer je tukaj lahko ali v smeri urinega kazalca ali pa proti.
        # "+" bo v smeri proti urinem kazalcu, "-" v nasprotni.
        niz = self.matrika.preberi_člen(koordinate)
        if je_škatla(niz):
            s = rotirane_smeri[niz[-1]]
            self.matrika.zamenjaj_člen(
                    koordinate,
                    škatla(len(niz), s if smer == "+" else nasprotne_smeri[s])
            )
        else:
            return True
            # raise ValueError("To ni škatla! Le škatle se da rotirati.")

    def prestavi_igralca(self, koordinate):
        if self.matrika_z_igralcem().preberi_člen(koordinate) == "":
            if koordinate.koordinate_gredo_v_matriko_dimenzij(self.matrika.širina, self.matrika.višina):
                self.koord_igralca.kopiraj_koordinate_od_drugega(koordinate)
            else:
                raise ValueError("Koordinate niso ustrezne! Koordinate " +
                                 koordinate +
                                 " ne gredo v matriko širine " +
                                 str(self.matrika.širina) +
                                 " in višine " +
                                 str(self.matrika.višina) + ".")
        else:
            return True
            # raise ValueError("Koordinate so že zasedene!")

    # tole je namenjeno le za prikaz igralcu:
    def matrika_z_igralcem(self):  # in tudi s poudarjenimi barvnimi škatlami
        kopija = self.matrika.kopiraj_sebe()

        # za upodobitev položajev barvnih škatel. Velike črke pomenijo barvne škatle
        for ključ in self.slovar_barvnih_škatel:
            koord = self.slovar_barvnih_škatel[ključ][0]
            kopija.zamenjaj_člen(koord, povečaj(kopija.preberi_člen(koord), int(ključ) - 1))
        kopija.zamenjaj_člen(self.koord_igralca, kopija.preberi_člen(self.koord_igralca) + "+")
        # "+" bo označeval igralca
        return kopija

    def __str__(self):
        return str(self.matrika_z_igralcem())

    __repr__ = __str__

    def poteza(self):
        self.št_potez += 1

    def preveri_okolico(self, smer):  # vrne True, kadar se lahko premakne v to smer
        nasprotna_smer = nasprotne_smeri[smer]
        # člen matrike, kjer je igralec:
        polje_z_igralcem = self.matrika.preberi_člen(self.koord_igralca)

        koord_od_drugega_polja = None
        if nasprotna_smer == znaki[1]:  # gremo v levo
            koord_od_drugega_polja = self.koord_igralca.vrni_levega_soseda()
        elif nasprotna_smer == znaki[0]:  # gremo v desno
            koord_od_drugega_polja = self.koord_igralca.vrni_desnega_soseda()
        elif nasprotna_smer == znaki[3]:  # gremo gor
            koord_od_drugega_polja = self.koord_igralca.vrni_zgornjega_soseda()
        elif nasprotna_smer == znaki[2]:  # gremo dol
            koord_od_drugega_polja = self.koord_igralca.vrni_spodnjega_soseda()
        drugo_polje = self.matrika.preberi_člen(koord_od_drugega_polja)
        # polje, kamor poskušamo iti z igralcem

        if drugo_polje == "!":
            return False  # skala

        for znak in drugo_polje:
            # če je kakšna škatla v napačno smer obrnjena:
            if znak != nasprotna_smer and znak != "-":
                return False  # ne more se igralec premakniti v to smer

        # preveriti moramo še notranjo velikost škatle:
        notranja_velikost_drugega_polja = 1
        # to je najmanjša možna škatla. Igralčeva velikost je 0,
        # zato še ravno lahko gre v to škatlo

        for znak in drugo_polje:
            if znak == "-":
                notranja_velikost_drugega_polja += 1
            else:
                break
        else:
            notranja_velikost_drugega_polja = float("inf")  # če drugo polje prazno polje

        # notranja in zunanja velikost posamezne škatle je vedno ista. Če pa imamo
        # več škatel (eno v drugi), potem pa to ni več res in je zunanja velikost večja

        # velikost igralca meri zunanjo velikost (notranja je irelevantna oz. je ni)

        # ampak najprej bomo razdelili igralčevo polje na ostanek in prenos:
        """
        Razdelili bomo igralčevo polje na del, ki se loči, in del, ki ostane.
        Operacija bo odvisna od smeri.

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

        ostanek, prenos = razdeli(polje_z_igralcem, smer)
        # sprejme prvotni člen in pa smer ter vrne nabor (ostane, gre stran)

        zunanja_velikost_prenosa = len(prenos)
        # dejansko je to velikost igralca (štejemo le škatle, ki grejo z njim)

        if notranja_velikost_drugega_polja > zunanja_velikost_prenosa:  # če paše notri

            # če so koordinate barvnih škatel iste kot koordinate igralca, potem
            # poglej, ali so barvne škatle v ostanku ali prenosu (saj v tem primeru
            # v polju mora biti prava usmerjenost na pravem mestu, saj poznamo
            # velikost škatel)

            # če je v ostanku, se nič ne spremeni. Če v prenosu, pa se.
            barvne_škatle_se_premaknejo = {}
            for ključ in self.slovar_barvnih_škatel:
                if self.slovar_barvnih_škatel[ključ][0] == self.koord_igralca:
                    # če so barvne škatle na istem mestu kot igralec
                    velikost = int(ključ)  # velikost barvne škatle je kar ključ
                    if len(prenos) >= velikost:
                        barvne_škatle_se_premaknejo[ključ] = True
                    else:
                        barvne_škatle_se_premaknejo[ključ] = False
                else:
                    barvne_škatle_se_premaknejo[ključ] = False

            nabor = (ostanek, prenos, drugo_polje, koord_od_drugega_polja, barvne_škatle_se_premaknejo)
            # [True, False, False, ...] po vrsti barvne škatle
            # v bistvu bo to slovar: {"1": True, "2": False, ...}, ne seznam

            zunanja_velikost_drugega_polja = len(drugo_polje)

            # self.velikost_igralca = zunanja_velikost_drugega_polja  # to je samo za škatle.
            # Če upoštevamo še prazna polja, moramo uporabiti spodnjo vrstico:
            self.velikost_igralca = max(zunanja_velikost_drugega_polja, zunanja_velikost_prenosa)
            # to je zato, ker ima prazno polje zunanjo velikost 0

            # zunanja velikost se ne spremeni, če gremo na prazno polje

            return nabor  # to je namesto True
        else:
            return False

    def premik_v_smer(self, smer):  # to bo uredilo matriko self.matrika
        # leva smer pomeni smer "z"
        if smer == znaki[0]:  # v levo
            if self.koord_igralca.x == 0:
                return False  # False vrnemo, če ni spremembe, True pa, če je
        if smer == znaki[1]:  # v desno
            if self.koord_igralca.x == self.matrika.širina - 1:
                return False
        if smer == znaki[2]:  # navzgor
            if self.koord_igralca.y == 0:
                return False
        if smer == znaki[3]:  # navzdol
            if self.koord_igralca.y == self.matrika.višina - 1:
                return False

        okolica = self.preveri_okolico(smer)  # tudi barvne škatle so notri vključene
        if okolica:  # če ni False
            ostanek, prenos, polje, koord_drugega_polja, b_škatle = okolica
            """
            Ustvarili bomo novo polje z naslednjo operacijo:

            "" + "" = ""
            "v" + "" = "v"
            "vz" + "--j" = "vzj"
            "-j" + "-z" ne gre
            "-s" + "--j" = "-sj"
            # operacija je tudi komutativna

            To operacijo bomo opisali v funkciji združi()
            """

            novo_polje = združi(prenos, polje)

            self.matrika.zamenjaj_člen(koord_drugega_polja, novo_polje)
            # posodobimo polje, kamor se je premaknil igralec

            self.matrika.zamenjaj_člen(self.koord_igralca, ostanek)
            # izpraznimo polje, kjer je bil igralec, razen če imamo ostanek

            self.koord_igralca.kopiraj_koordinate_od_drugega(koord_drugega_polja)
            # posodobimo koordinate

            # tukaj posodobimo še morebitne koordinate barvnih škatel
            for ključ in b_škatle:
                if b_škatle[ključ]:
                    self.slovar_barvnih_škatel[ključ][0].kopiraj_koordinate_od_drugega(koord_drugega_polja)
            return True  # igralec se premakne
        return False  # igralec se ne premakne

    # za vsako polje v matriki lahko definiramo največjo velikost igralca (v kako
    # veliki škatli je lahko), da še lahk gre na tisto polje. Če je prazno
    # polje, je največja velikost neomejena.

    # igralec po premiku dobi novo velikost, ki ni nujno ista kot ravnokar
    # definirana količina. Dobimo jo pač s primerjavo členov matrike

    def preveri_ali_na_cilju(self):
        # pri naborih nam ni treba skrbet za kazalce
        koord_barvnih_škatel = [self.slovar_barvnih_škatel[ključ][0] for ključ in self.slovar_barvnih_škatel.keys()]
        return vsi_elementi_seznama_so_isti(koord_barvnih_škatel)


class VsiNivoji:  # v vrstnem redu - ampak ne vsi, kr lah mamo tut custom level. Torej bomo imeli slovar
    """
    Vsebuje slovar "slovar_nivojev", ki pod ime nivoja shrani nabor, ki vsebuje podatke o:
    - začetnem stanju nivoja (se tekom igre ne spremeni)
    - rekord oz. najmanjše število potez, ki so kateremukoli igralcu do zdaj bile potrebne za rešitev nivoja
    """
    def __init__(self, datoteka_z_nivoji=pridobi_relativno_pot("nivoji.json")):
        self.datoteka_z_nivoji = datoteka_z_nivoji
        # oblika: {"1": ((seznam_seznamov, začetni_koord, seznam_naborov_barvnih_škatel),
        # min_št_potez), "2": ..., "custom_level": ...}

        # ključ in ime bosta vedno enaka (če bomo sploh imel ime) - ne ne bomo
        with open(self.datoteka_z_nivoji, "r", encoding="utf-8") as f:
            self.slovar_nivojev = json.load(f)

        # to je samo število oštevilčenih nivojev (štetje se začne z 1)
        self.število_nivojev = max([int(ključ) for ključ in self.slovar_nivojev.keys() if ključ.isdigit()])
        # vsi ključi bodo stringi

    def preberi_iz_datoteke(self):
        with open(self.datoteka_z_nivoji, "r", encoding="utf-8") as f:
            self.slovar_nivojev = json.load(f)

    def naloži_v_datoteko(self):
        with open(self.datoteka_z_nivoji, "w", encoding="utf-8") as f:
            json.dump(self.slovar_nivojev, f, indent=4)

    def vrni_prazno_ime(self, default_ime="Nepoimenovan nivo"):
        dolžina = len(default_ime)
        seznam = [ključ[dolžina + 1:] for ključ in self.slovar_nivojev.keys() if ključ[:dolžina] == default_ime]
        if len(seznam) == 0:
            return default_ime
        else:
            število = max([int(niz) for niz in seznam + ["0"] if niz.isdigit()]) + 1
            # torej if niz != ""

            return default_ime + " " + str(število)

    def vrni_nivo(self, id_trenutnega_nivoja):
        return Nivo(*(deepcopy(self.slovar_nivojev[id_trenutnega_nivoja][0])))
        # če ne kopiramo oz. naredimo samo .copy, bodo nekateri pointerji še
        # kar kazali na isto mesto v pomnilniku. Takrat bi se z igranjem nivoja
        # hkrati spreminjal tudi self.slovar_nivojev, kar pa nočemo. Nivoji se
        # ne smejo spreminjati v objektih tipa VsiNivoji.

    def vrni_rekord(self, id_trenutnega_nivoja):
        return self.slovar_nivojev[id_trenutnega_nivoja][1]

    def dodaj_nivo(self, ime_nivoja, nivo):
        if ime_nivoja in self.slovar_nivojev.keys():
            raise ValueError("Nivo s tem imenom že obstaja!")  # to se ne bi smelo zgoditi
        self.slovar_nivojev[ime_nivoja] = [nivo.vrni_parametre(), float("inf")]
        # VsiNivoji ne vsebuje nivojev, le potrebne podatke za izdelavo le-teh
        self.naloži_v_datoteko()

    def obnovi_rekord(self, ime_nivoja, nov_rekord):
        # nov rekord je samo število potez v trenutni igri
        # ni nujno, da bo nov_rekord dejanski rekord
        dozdajšnji_rekord = self.vrni_rekord(ime_nivoja)  # rekord nivoja
        self.slovar_nivojev[ime_nivoja][1] = min(nov_rekord, dozdajšnji_rekord)
        self.naloži_v_datoteko()
        stanje = None if nov_rekord == dozdajšnji_rekord else (nov_rekord < dozdajšnji_rekord)
        return (stanje, dozdajšnji_rekord)


class VseIgre:
    """
    Vsebuje slovar "stanja", ki pod id uporabnika (ki ga dobimo iz piškotka) shrani nabor štirih spremenljivk, v tem vrstnem redu:
    - ime nivoja, ki ga uporabnik trenutno igra
    - stanje nivoja, ki je objekt tipa Nivo
    - trenutni objekt, ki je označen v urejevalcu nivojev
    - napaka, ki opozori uporabnika o neveljavnem ukazu. To je nabor, prvi člen je ime napake, drugi pa vnos, ki je napako povzročil. Če vnosa ni, je None.
    """
    # pod userid je shranjen
    def __init__(self):
        self.stanja = {}

        # {iduporabnika: (imelevela, stanjelevela (oz. kar level sam),
        # trenutniobjekt, napaka), ...}

        # stanje levela je istega formata kot v VsiNivoji

        # trenutniobjekt je označen objekt v urejevalniku (recimo
        # črna škatla, te pa te velikosti).
        # Če nismo v urejevalniku, je None

    def vrni_nivo(self, id_igralca):
        return self.stanja[id_igralca][1]

    def vrni_ime(self, id_igralca):
        return self.stanja[id_igralca][0]

    def vrni_objekt(self, id_igralca):
        return self.stanja[id_igralca][2]

    def vrni_napako(self, id_igralca):
        return self.stanja[id_igralca][3]

    def spremeni_ime(self, id_igralca, novo_ime):
        _, lvl, obj, napaka = self.stanja[id_igralca]
        self.stanja[id_igralca] = (novo_ime, lvl, obj, napaka)

    def spremeni_objekt(self, id_igralca, nov_objekt):
        ime, lvl, _, napaka = self.stanja[id_igralca]
        self.stanja[id_igralca] = (ime, lvl, nov_objekt, napaka)

    def spremeni_napako(self, id_igralca, napaka):
        ime, lvl, obj, _ = self.stanja[id_igralca]
        self.stanja[id_igralca] = (ime, lvl, obj, napaka)


def vrni_prazen_nivo(širina, višina):
    # imel bo igralca v levem zgornjem kotu, potem pa dve barvni škatli:
    # manjšo desno zgoraj, večjo desno spodaj
    seznam_seznamov = []
    for i in range(višina):
        seznam_seznamov.append([])
        for j in range(širina):
            seznam_seznamov[-1].append("")
    seznam_seznamov[0][širina - 1] = znaki[2]
    seznam_seznamov[višina - 1][širina - 1] = "-" + znaki[2]
    return Nivo(
            seznam_seznamov,
            (0, 0),
            [(širina - 1, 0),
             (širina - 1, višina - 1)])


class Uporabniki:
    """
    Vsebuje slovar "idji", ki pod uporabnikov id, v tem vrstnem redu, shrani:
    - seznam naborov, ki vsebujejo ime nivoja, ki ga je ta uporabnik že izdelal, in najmanjše število potez, ki jih je potreboval
    - ime nivoja, ki ga ima uporabnik trenutno odprtega v urejevalcu nivojev
    - objekt Nivo, ki je trenutno odprt v urejevalcu nivojev
    """
    def __init__(self, datoteka_s_stanjem=pridobi_relativno_pot("uporabniki.json")):
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.idji = {}
        # na začetku vedno prazen slovar, saj bomo takoj prebrali iz datoteke

    def preberi_iz_datoteke(self):
        # ko se naloži seznam ven, ga moramo prevesti v množico,
        # če je v originalu to bila množica
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as f:
            placeholder_slovar = json.load(f)
            # {1: (["1", "2", "4"], Nivo()), 2: ...}
            # namesto bomo imeli ([dokončani nivoji], ime, stanje_nivoja)
        for ključ in placeholder_slovar:
            stanje_nivoja = placeholder_slovar[ključ][2]
            if stanje_nivoja is None:
                nivo = stanje_nivoja
            else:
                nivo = Nivo(*stanje_nivoja)

            self.idji[ključ] = (placeholder_slovar[ključ][0],
                                placeholder_slovar[ključ][1],
                                nivo)

    def naloži_v_datoteko(self):
        # nočemo, da se s spreminjanjem slovarja "placeholder_slovar"
        # spreminja tudi self.idji
        placeholder_slovar = deepcopy(self.idji)
        for ključ in placeholder_slovar:
            nivo = self.vrni_nivo(ključ)
            if nivo is None:
                stanje_nivoja = nivo
            else:
                stanje_nivoja = nivo.vrni_parametre()
            rešeni_nivoji = self.vrni_rešene_nivoje(ključ)
            ime = self.vrni_ime(ključ)
            placeholder_slovar[ključ] = (rešeni_nivoji, ime, stanje_nivoja)
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as f:
            json.dump(placeholder_slovar, f, indent=4)

    def prost_id_igre(self):
        return str(max([int(niz) for niz in self.idji.keys()], default=-1) + 1)
        # json pretvori vse celoštevilske ključe slovarjev v nize

    def dokončal_nivo(self, id_uporabnika, ime_nivoja, poteze):
        nivoji, ime, urejevalnik = self.idji[id_uporabnika]
        stanje = False
        for indeks, nabor in enumerate(nivoji):
            nivo, št_potez = nabor
            if nivo == ime_nivoja:
                if poteze < št_potez:  # nov rekord
                    stanje = True
                elif poteze <= št_potez:
                    stanje = None
                poteze = min(poteze, št_potez)  # posodobi osebni rekord za ta nivo
                nivoji[indeks] = (ime_nivoja, poteze)
                break
        else:  # če se break ne izvede
            nivoji.append((ime_nivoja, poteze))
            # če je uporabnik ta nivo dokončal prvič
            št_potez = float("inf")
        self.idji[id_uporabnika] = (nivoji, ime, urejevalnik)
        self.naloži_v_datoteko()
        return (stanje, št_potez)
        # vrne False, če ni novega rekorda oz. smo prvič dokončali ta nivo, 
        # drugače True oz. None, če pride do izenačenja

    def spremenil_ime(self, id_uporabnika, novo_ime):
        nivoji, _, nivo = self.idji[id_uporabnika]
        self.idji[id_uporabnika] = (nivoji, novo_ime, nivo)
        self.naloži_v_datoteko()

    def uredil_nivo(self, id_uporabnika, nivo):
        # nivo je pač spremenjeno stanje nivoja, ki se ga obdeluje.
        # Ime je tukaj shranjeno zraven

        nivoji, ime, _ = self.idji[id_uporabnika]
        self.idji[id_uporabnika] = (nivoji, ime, nivo)
        self.naloži_v_datoteko()

    def dodaj_uporabnika(self):
        id_uporabnika = self.prost_id_igre()

        # None je, če ni nobenega levela shranjenega v urejevalniku -
        # drugače pa celotno stanje levela, vključno z imenom
        self.idji[id_uporabnika] = ([], None, None)

        self.naloži_v_datoteko()
        return id_uporabnika

    def vrni_nivo(self, id_uporabnika):
        return self.idji[id_uporabnika][2]

    def vrni_ime(self, id_uporabnika):
        return self.idji[id_uporabnika][1]

    def vrni_rešene_nivoje(self, id_uporabnika):
        return self.idji[id_uporabnika][0]
