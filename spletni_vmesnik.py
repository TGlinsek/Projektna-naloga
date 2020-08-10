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

def odpri_nivo(id_levela, urejanje=False):
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    nivo = vsi_nivoji.vrni_nivo(id_levela)

    vse_igre.stanja[id_uporabnika] = (id_levela, nivo, "+" if urejanje else None)  # tak je format


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


@bottle.post('/ustvarjanje_igre/')
def iniciiranje_igre():
    # testni_seznam.clear()  # izbrišemo prejšnjo igro
    # pozor: tukaj ne moremo napisati kar testni_seznam = [], ker je potem to nova, lokalna spremenljivka. Globalna se torej ne spremeni.

    id_prvega_levela = "1"

    odpri_nivo(id_prvega_levela)

    bottle.redirect('/dejanska_igra/')

@bottle.get('/dejanska_igra/')
def igranje():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    return bottle.template(pot("igrica.tpl"), game=vse_igre.vrni_level(id_uporabnika), ime=vse_igre.vrni_ime(id_uporabnika), max_stevilo=vsi_nivoji.število_nivojev)

@bottle.post('/dejanska_igra/')
def poteza():
    id_uporabnika = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")

    smer1 = bottle.request.forms.getunicode('smer')
    smer1 = smer1.lower()
    vse_igre.vrni_level(id_uporabnika).premik_v_smer(smer1)
    bottle.redirect('/dejanska_igra/')

# Seznam levelov
@bottle.post('/vsi_leveli/')  # to lahk mogoč zbrišemo
def nalaganje_levelov():
    bottle.redirect('/seznam_levelov/')

@bottle.get('/seznam_levelov/')
def seznam():
    uporabnikov_id = bottle.request.get_cookie('piskotek_ki_pripada_temu_uporabniku', secret="SKRIVNOST")  # pridobi id od uporabnika, da dobimo seznam nivojev, ki jih je že zigral
    return bottle.template(pot("seznam.tpl"), vsi_nivoji=sorted(vsi_nivoji.slovar_nivojev.keys()), reseni_nivoji=uporabniki.idji[uporabnikov_id][0])

@bottle.post('/Level_n/<ime_nivoja>/')
def pridobivanje_levela(ime_nivoja):
    # naloži level
    # vse_igre.shrani ime_nivoja pod id_uporabnika
    # zdaj pa ustvarimo nivo iz podatka o imenu

    odpri_nivo(ime_nivoja)

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
    odpri_nivo(ime_nivoja, urejanje=True)
    # tut tk bi lah, sam bomo rajš šparal s piškotki
    # bottle.response.set_cookie('ime_nivoja', ime_nivoja, secret="SKRIVNOST", expires=datum_ćez_7_dni)
    bottle.redirect('/urejevalec/')

# Urejevalec
@bottle.get('/urejevalec/')
def urejanje():
    return bottle.template(pot("urejevalec.tpl"))

# v urejevalcu bo še gumb, kjer lahko shranimo svoj level. Tam bo program zahteval, da si izmislimo ime za ta level. Potem gre v seznam levelov

# level lahko tudi "lajkamo"/"dislajkamo". Ko končamo level, se shrani informacija o tem, da smo level končali, na strežnik. Če lajkamo/dislajkamo, se tudi to shrani. Na koncu se izračuna razmerje in ostala statistika



# nujno je treba dodati path, če imamo folder namesto slike
@bottle.get('/Projektna-naloga/<mapa:path>')  # tu je lahko / na konc al pa ne
def serve_pictures(mapa):
    return bottle.static_file(mapa, root="UVP\\Projektna-naloga")


bottle.run(reloader=True, debug=True)