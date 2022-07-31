import bottle
import model
import datetime

import os

from pathlib import Path

cwd = os.getcwd()
prava_pot = os.path.realpath(__file__)  # pot do tele datoteke
starš = Path(prava_pot).parent  # pot do mape, kjer se nahaja trenutna datoteka
relativna_pot = os.path.relpath(starš, start=os.getcwd())


# starš = Path(__file__).parent
abs_pot = (starš / "views")  # iz relativne poti naredi absolutno


# views_veja = os.path.relpath(abs_pot, starš.parent.parent)  # views_veja = "UVP\\Projektna-naloga\\views"
veja_za_slike = os.path.relpath(starš, starš.parent.parent)

# views_veja = "Projektna-naloga\\views"
# veja_za_slike = "Projektna-naloga"
# tudi to dvoje bi šlo

# povezava_za_bazo = os.path.relpath((abs_pot / "osnova.tpl").resolve(), starš.parent.parent)
povezava_za_bazo = os.path.relpath(starš / "views" / "osnova.tpl", start=os.getcwd())


datum_čez_10_let = datetime.datetime.now() + datetime.timedelta(days=(365 * 10))

# ta objekt bo spremljal vse dosedaj zasedene id-je
# (to so samo integerji (oz. integerji, pretvorjeni v nize)).
# Ima še metodo, ki priredi nov unikaten id:
uporabniki = model.Uporabniki()
uporabniki.preberi_iz_datoteke()

vsi_nivoji = model.VsiNivoji()

vse_igre = model.VseIgre()


"""
def pot(ime_datoteke):  # ime je npr. igra.tpl
    return os.path.join(views_veja, ime_datoteke)
"""


def odpri_nivo(id_levela):
    nivo = vsi_nivoji.vrni_nivo(id_levela)
    return nivo


@bottle.get('/')
def naslovna_stran():
    # to je None, če je to prvi obisk
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', 
                                 secret="SKRIVNOST")
    if not id_uporabnika:
        return bottle.template(str(relativna_pot) + "\\views\\naslovnica.tpl", povezava_za_bazo=povezava_za_bazo)
    
    return bottle.template(str(relativna_pot) + "\\views\\glavni_meni.tpl",
                           povezava_za_bazo=povezava_za_bazo,
                           št_rešenih_nivojev=len(uporabniki.vrni_rešene_nivoje(id_uporabnika)),
                           št_vseh_nivojev=len(vsi_nivoji.slovar_nivojev)
                           )
                           # tukaj zraven vstavimo podatek o številu nivojev, ki jih je 
                           # uporabnik končal, in pa vseh nivojev, ki so na voljo


@bottle.post('/nalaganje/')
def obisk_strani():
    ne_prvi_obisk = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', 
                                 secret="SKRIVNOST")
    if ne_prvi_obisk:
        pass
        # print("Ponovno si obiskal to stran!")
    else:
        id_uporabnika = uporabniki.dodaj_uporabnika()
        # prvič, ko uporabnik pride na stran, se mu doda piškotek
        bottle.response.set_cookie('piskotek_ki_pripada_temu_uporabniku',
                                   id_uporabnika,
                                   secret="SKRIVNOST",
                                   expires=datum_čez_10_let,
                                   path='/')  
                                   # brez path parametra si bottle za path izbere 
                                   # ime te metode, torej piškotek ni 
                                   # več dostopen vsem stranem

        # ta piškotek bo shranil seznam vseh imen nivojev,
        # ki jih je uporabnik že dokončal,
        # in pa še trenutni nivo v urejevalniku.
        # To vse shrani v json datoteko
    bottle.redirect('/')


@bottle.post('/nazaj_na_prvo_stran/')
def prva_stran():
    bottle.redirect('/')


@bottle.get('/igra/')
def igranje():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    return bottle.template(str(relativna_pot) + "\\views\\igrica.tpl",
                           igra=vse_igre.vrni_nivo(id_uporabnika),
                           ime=vse_igre.vrni_ime(id_uporabnika),
                           max_stevilo=vsi_nivoji.število_nivojev,
                           napaka=vse_igre.vrni_napako(id_uporabnika),
                           povezava_za_bazo=povezava_za_bazo,
                           reseni_nivoji=uporabniki.vrni_rešene_nivoje(id_uporabnika),
                           nivoji=vsi_nivoji.slovar_nivojev
                           )  
                           # dodali smo še seznam vseh uporabnikovih rešenih nivojev in pa slovar 
                           # vseh nivojev, da lahko sproti spremljamo "podiranje rekordov" 
                           # in to uporabniku tudi sporočimo


@bottle.post('/igra/')
def poteza():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku',
                                              secret="SKRIVNOST")

    vse_igre.spremeni_napako(id_uporabnika, None)  # resetiramo napako

    smer1 = bottle.request.forms.getunicode('smer')
    smer1 = smer1.lower()
    if smer1 not in model.znaki:
        vse_igre.spremeni_napako(id_uporabnika, ("smer", smer1))
    else:
        nivo = vse_igre.vrni_nivo(id_uporabnika)

        # ta vrstica premakne igralca, če ga lahko. 
        # Informacija o tem, ali se igralec premakne, se shrani v "premik"
        premik = nivo.premik_v_smer(smer1)

        if premik:
            nivo.poteza()
        if nivo.preveri_ali_na_cilju():
            ime_nivoja = vse_igre.vrni_ime(id_uporabnika)
            stanje_osebnega_rekorda = uporabniki.dokončal_nivo(id_uporabnika, ime_nivoja, nivo.št_potez)
            stanje_rekorda = vsi_nivoji.obnovi_rekord(ime_nivoja, nivo.št_potez)
            vse_igre.spremeni_napako(id_uporabnika, ("rekord", *stanje_rekorda, *stanje_osebnega_rekorda))  # dejansko ni napaka
    bottle.redirect('/igra/')


# Seznam nivojev
@bottle.post('/shrani_nivo/')
def shranjevanje_nivoja():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku',
                                              secret="SKRIVNOST")
    vse_igre.spremeni_napako(id_uporabnika, None)  # izbrišemo sporočilo za napako

    ime = uporabniki.vrni_ime(id_uporabnika)
    nivo = uporabniki.vrni_nivo(id_uporabnika)

    napaka = vsi_nivoji.dodaj_nivo(ime, nivo)
    if napaka:
        vse_igre.spremeni_napako(id_uporabnika, ("nivo", napaka))  # ime je zasedeno
    bottle.redirect('/seznam_nivojev/')


@bottle.post('/pridobi_seznam/')
def pridobi():
    bottle.redirect('/seznam_nivojev/')


@bottle.get('/seznam_nivojev/')
def seznam():
    # pridobi id od uporabnika, da dobimo seznam nivojev, ki jih je že dokončal
    uporabnikov_id = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku',
                                               secret="SKRIVNOST")

    # izbrišemo sporočilo za napako oz. ustvarimo 
    # vrednost za tega uporabnika v slovarju vse_igre.stanja
    vse_igre.stanja[uporabnikov_id] = (None, None, None, None)

    return bottle.template(str(relativna_pot) + "\\views\\seznam.tpl",
                           vsi_nivoji=vsi_nivoji.slovar_nivojev,
                           reseni_nivoji=uporabniki.vrni_rešene_nivoje(uporabnikov_id),
                           povezava_za_bazo=povezava_za_bazo)


@bottle.post('/nalaganje_nivoja/<ime_nivoja>/')
def pridobivanje_levela(ime_nivoja):
    # naloži nivo
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku',
                                              secret="SKRIVNOST")
    nivo = odpri_nivo(ime_nivoja)
    vse_igre.stanja[id_uporabnika] = (ime_nivoja, nivo, None, None)

    bottle.redirect('/igra/')


@bottle.post('/urejanje_nivoja/<ime_nivoja>/')
def prid_levela(ime_nivoja):
    # tukaj naložimo nivo, za urejanje v urejevalcu nivojev

    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku',
                                              secret="SKRIVNOST")
    nivo = odpri_nivo(ime_nivoja)

    # ne potrebujemo imena in nivoja od prej, zato je None
    # (vse_igre namreč ne shranjuje informacij urejevalnika)
    vse_igre.stanja[id_uporabnika] = (None, None, "+", None)

    # priredi novo, unikatno ime, tako da dodamo število na konec
    uporabniki.spremenil_ime(id_uporabnika, vsi_nivoji.vrni_prazno_ime(ime_nivoja))

    uporabniki.uredil_nivo(id_uporabnika, nivo)

    bottle.redirect('/urejevalec/')


@bottle.post('/urejanje_nivoja/')
def prazen_nivo():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', 
                                              secret="SKRIVNOST")

    širina = int(bottle.request.forms.getunicode('sirina'))
    višina = int(bottle.request.forms.getunicode('visina'))

    nivo = model.vrni_prazen_nivo(širina, višina)
    vse_igre.stanja[id_uporabnika] = (None, None, "+", None)

    # vrni ime, ki se začne z "Nepoimenovan nivo", sledi mu pa neko število
    uporabniki.spremenil_ime(id_uporabnika, vsi_nivoji.vrni_prazno_ime())

    uporabniki.uredil_nivo(id_uporabnika, nivo)

    bottle.redirect('/urejevalec/')


# Urejevalec
@bottle.get('/urejevalec/')
def urejanje():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', 
                                              secret="SKRIVNOST")

    return bottle.template(str(relativna_pot) + "\\views\\urejevalec.tpl",
                           igra=uporabniki.vrni_nivo(id_uporabnika),
                           ime=uporabniki.vrni_ime(id_uporabnika),
                           izbran_objekt=vse_igre.vrni_objekt(id_uporabnika),
                           napaka=vse_igre.vrni_napako(id_uporabnika),
                           povezava_za_bazo=povezava_za_bazo)


@bottle.post('/urejevalec/<niz>/')
def poteza_urejanje(niz):
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', 
                                              secret="SKRIVNOST")
    vse_igre.spremeni_napako(id_uporabnika, None)  # izbrišemo sporočilo za napako

    # niz je lahko oblike koordx-y, puscica1, puscica2, -, +, !, w, W, -w, -W itd.
    if niz[:5] == "koord":
        zadnji_del = niz[5:]
        indeks = zadnji_del.index("-")
        x = int(zadnji_del[:indeks])
        y = int(zadnji_del[indeks + 1:])

        nivo = uporabniki.vrni_nivo(id_uporabnika)
        objekt = vse_igre.vrni_objekt(id_uporabnika)
        koord = model.Koordinate((x, y))
        if objekt[:7] == "puscica":
            zadnji_znak = objekt[-1]
            znak = "+" if zadnji_znak == "1" else "-"  # zadnji_znak je lahko samo "1" ali pa "2"
            napaka = nivo.rotiraj_škatlo(koord, znak)
            if napaka:
                vse_igre.spremeni_napako(id_uporabnika, ("rotacija", None))
        elif objekt == "+":
            napaka = nivo.prestavi_igralca(koord)
            if napaka:
                vse_igre.spremeni_napako(id_uporabnika, ("polje", None))
        elif objekt == "-":
            napaka = nivo.odstrani_element(koord)
            if napaka:
                if napaka == 2:
                    vse_igre.spremeni_napako(id_uporabnika, ("igralec", None))
                else:
                    vse_igre.spremeni_napako(id_uporabnika, ("škatla", None))
                    # škatli sta manj kot dve
        elif objekt == "!":
            napaka = nivo.dodaj_element(koord, "!")
            if napaka:
                vse_igre.spremeni_napako(id_uporabnika, ("polje", None))
        else:  # škatla
            črka = objekt[-1]
            velikost = len(objekt)
            if črka.lower() == črka:  # če mala črka
                napaka = nivo.dodaj_škatlo(velikost, koord)  # najmanjša velikost je 1
                if napaka:
                    vse_igre.spremeni_napako(id_uporabnika, ("polje", None))
            elif črka.upper() == črka:  # če velika črka
                napaka = nivo.dodaj_barvno_škatlo(velikost, koord)
                if napaka:
                    vse_igre.spremeni_napako(id_uporabnika, ("polje", None))
            else:
                raise ValueError("Škatla ni ne velika ne mala!")  # to se naj ne bi zgodilo
    else:  # sprememba objekta:  vse_igre.spremeni_objekt(id_uporabnika, nov_objekt)
        vse_igre.spremeni_objekt(id_uporabnika, niz)  # tu se samo spremeni objekt ki je shranjen
        # objekt je lahko tudi puscica1 ali puscica2

    bottle.redirect('/urejevalec/')


@bottle.post('/urejevalec/')
def urejanje_imena():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', 
                                              secret="SKRIVNOST")
    vse_igre.spremeni_napako(id_uporabnika, None)  # izbrišemo sporočilo za napako
    novo_ime = bottle.request.forms.getunicode('ime')  # podpora za šumnike
    stopnja = bottle.request.forms.getunicode('stopnja')
    if stopnja in ["2", "3"]:
        nivo = uporabniki.vrni_nivo(id_uporabnika)
        nivo.velikostna_stopnja = int(stopnja)
    else:
        if novo_ime is None:
            raise ValueError("Novo ime ima vrednost None!")  # to se naj ne bi nikoli zgodilo
        ime = novo_ime.strip()
        if ime == "":
            vse_igre.spremeni_napako(id_uporabnika, ("ime", novo_ime))
            # raise ValueError("Neveljavno ime: " + novo_ime + "!")
        else:
            if ime in vsi_nivoji.slovar_nivojev.keys():
                vse_igre.spremeni_napako(id_uporabnika, ("nivo", novo_ime))
                # raise ValueError("Ime: " + novo_ime + " je že zasedeno!")
            else:
                uporabniki.spremenil_ime(id_uporabnika, ime)

    bottle.redirect('/urejevalec/')


# nujno je treba dodati path, če imamo folder namesto slike
@bottle.get('/Projektna-naloga/<mapa:path>')
def serve_pictures(mapa):
    return bottle.static_file(mapa, root=veja_za_slike)


bottle.run()
