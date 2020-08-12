import bottle
import model
import datetime

import os

veja = "UVP\\Projektna-naloga\\views"
# testni_seznam = []  # ima shranjene trenutne levele (med igranjem)

datum_čez_30_dni = datetime.datetime.now() + datetime.timedelta(days=30)
datum_ćez_7_dni = datetime.datetime.now() + datetime.timedelta(days=7)

uporabniki = model.Uporabniki()  # ta objekt bo spremljal vse dosedaj zasedene id-je (to so samo integerji). Ima še metodo, ki priredi nov unikaten id
uporabniki.preberi_iz_datoteke()

vsi_nivoji = model.VsiNivoji()

vse_igre = model.VseIgre()


def pot(ime_datoteke):  # ime je npr. igra.tpl
    return os.path.join(veja, ime_datoteke)

def odpri_nivo(id_levela):
    nivo = vsi_nivoji.vrni_nivo(id_levela)
    return nivo


@bottle.get('/')
def obisk_strani():
    if bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST"):
        print("Ponovno si obiskal to stran!")
    else:
        # prvič, ko uporabnik pride na stran, se mu doda piškotek 
        bottle.response.set_cookie('piskotek_ki_pripada_temu_uporabniku', uporabniki.dodaj_uporabnika(), secret="SKRIVNOST", expires=datum_čez_30_dni)
        # ta piškotek bo shranil seznam vseh imen nivojev, ki jih je uporabnik že zigral, in pa še trenutni level v urejevalniku. To vse shrani v json datoteko

        # getamo ga samo takrat, ko rešimo kak level (torej, ko zmagamo) ali pa urejamo kak level
    bottle.redirect('/dobrodošel/')

@bottle.get('/dobrodošel/')
def naslovna_stran():
    return bottle.template(pot("naslovnica.tpl"))


@bottle.get('/dejanska_igra/')
def igranje():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    return bottle.template(pot("igrica.tpl"), game=vse_igre.vrni_nivo(id_uporabnika), ime=vse_igre.vrni_ime(id_uporabnika), max_stevilo=vsi_nivoji.število_nivojev)

@bottle.post('/dejanska_igra/')
def poteza():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")
    # tu dodaj zigran level v seznam
    smer1 = bottle.request.forms.getunicode('smer')
    smer1 = smer1.lower()
    vse_igre.vrni_nivo(id_uporabnika).premik_v_smer(smer1)
    bottle.redirect('/dejanska_igra/')

# Seznam levelov
@bottle.post('/shrani_nivo/')
def shranjevanje_nivoja():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    ime = uporabniki.vrni_ime(id_uporabnika)
    nivo = uporabniki.vrni_nivo(id_uporabnika)

    vsi_nivoji.dodaj_nivo(ime, nivo)
    bottle.redirect('/seznam_levelov/')

@bottle.get('/seznam_levelov/')
def seznam():
    uporabnikov_id = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")  # pridobi id od uporabnika, da dobimo seznam nivojev, ki jih je že zigral

    return bottle.template(pot("seznam.tpl"), vsi_nivoji=sorted(vsi_nivoji.slovar_nivojev.keys()), reseni_nivoji=uporabniki.vrni_rešene_nivoje(uporabnikov_id))

@bottle.post('/Level_n/<ime_nivoja>/')
def pridobivanje_levela(ime_nivoja):
    # naloži level
    # vse_igre.shrani ime_nivoja pod id_uporabnika
    # zdaj pa ustvarimo nivo iz podatka o imenu
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")
    nivo = odpri_nivo(ime_nivoja)
    vse_igre.stanja[id_uporabnika] = (ime_nivoja, nivo, None)
    # tut tk bi lah, sam bomo rajš šparal s piškotki:
    # bottle.response.set_cookie('ime_nivoja', ime_nivoja, secret="SKRIVNOST", expires=datum_ćez_7_dni)
    bottle.redirect('/dejanska_igra/')

@bottle.post('/Level_n_urejanje/<ime_nivoja>/')
def prid_levela(ime_nivoja):
    # tukaj iniciiramo level, za urejanje v urejevalcu levelov
    """
    vse_igre.shrani ime_nivoja pod id_uporabnika (imelevela, (seznam_seznamov, začetni_koord, seznam_naborov_barvnih_škatel), objekt)  - namest nabora na drugem mestu bo kar objekt Nivo
    imelevela dobimo iz linka, ostalo iz VsiNivoji
    če trenutno nismo na nivoju, pol se pač ti podatki ne spreminjajo (tudi ne izbrišejo se)
    """
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")
    nivo = odpri_nivo(ime_nivoja)
    
    # vse_igre.spremeni_objekt(id_uporabnika, "+")  # to ne gre, saj še slovar pod tem ključem sploh ni nujno definiran
    # ne potrebujemo imena in levela od prej (vse_igre ne shranjuje informacij urejevalnika), zato je None
    vse_igre.stanja[id_uporabnika] = (None, None, "+")

    uporabniki.spremenil_ime(id_uporabnika, ime_nivoja)
    uporabniki.uredil_nivo(id_uporabnika, nivo)
    # tut tk bi lah, sam bomo rajš šparal s piškotki
    # bottle.response.set_cookie('ime_nivoja', ime_nivoja, secret="SKRIVNOST", expires=datum_ćez_7_dni)
    bottle.redirect('/urejevalec/')

# Urejevalec
@bottle.get('/urejevalec/')
def urejanje():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    return bottle.template(pot("urejevalec.tpl"), game=uporabniki.vrni_nivo(id_uporabnika), ime=uporabniki.vrni_ime(id_uporabnika), izbran_objekt=vse_igre.vrni_objekt(id_uporabnika))

# v urejevalcu bo še gumb, kjer lahko shranimo svoj level. Tam bo program zahteval, da si izmislimo ime za ta level. Potem gre v seznam levelov

# level lahko tudi "lajkamo"/"dislajkamo". Ko končamo level, se shrani informacija o tem, da smo level končali, na strežnik. Če lajkamo/dislajkamo, se tudi to shrani. Na koncu se izračuna razmerje in ostala statistika

@bottle.post('/urejevalec/<niz>/')
def poteza_urejanje(niz):
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")
    # niz je lahko oblike koordx-y, puscica1, puscica2, -, +, !, s, S, -s, -S itd.
    if niz[:5] == "koord":  # izbran objekt se ne spremeni, le kopira se ga in se ga vstavi v nivo
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
            nivo.rotiraj_škatlo(koord, znak)
        elif objekt == "+":
            nivo.prestavi_igralca(koord)
        elif objekt == "-":
            nivo.odstrani_element(koord)
        elif objekt == "!":
            nivo.dodaj_element(koord, "!")
        else:  # škatla
            črka = objekt[-1]
            velikost = len(objekt)
            if črka.lower() == črka:  # če mala črka
                nivo.dodaj_škatlo(velikost, koord)  # najmanjša velikost je 1
            elif črka.upper() == črka:  # če velika črka
                nivo.dodaj_barvno_škatlo(velikost, koord)
            else:
                raise ValueError("Škatla ni ne velika ne mala!")
    else:  # sprememba objekta:  vse_igre.spremeni_objekt(id_uporabnika, nov_objekt)
        vse_igre.spremeni_objekt(id_uporabnika, niz)  # tu se samo spremeni objekt ki je shranjen
        # objekt je lahko tudi puscica1 ali puscica2
    
    # te vrstice morda ne potrebujemo, saj se objekt sam od sebe spremeni
    # uporabniki.uredil_nivo(id_uporabnika, nivo)
    
    bottle.redirect('/urejevalec/')


@bottle.post('/urejevalec/')
def urejanje_imena():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")
    novo_ime = bottle.request.forms.getunicode('ime')  # podpora za šumnike
    if novo_ime is None:
        raise ValueError("Novo ime ima vrednost None!")  # to se naj ne bi nikoli zgodilo
    ime = novo_ime.strip()
    if ime == "":
        raise ValueError("Neveljavno ime: " + novo_ime + "!")
    else:
        uporabniki.spremenil_ime(id_uporabnika, ime)

    bottle.redirect('/urejevalec/')




# nujno je treba dodati path, če imamo folder namesto slike
@bottle.get('/Projektna-naloga/<mapa:path>')  # tu je lahko / na konc al pa ne
def serve_pictures(mapa):
    return bottle.static_file(mapa, root="UVP\\Projektna-naloga")


bottle.run(reloader=True, debug=True)