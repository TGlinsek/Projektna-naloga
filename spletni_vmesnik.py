import bottle
import model

import os

veja = "UVP\\Projektna-naloga\\views"
testni_seznam = []

def pot(ime_datoteke):  # ime je npr. igra.tpl
    return os.path.join(veja, ime_datoteke)

@bottle.get('/')
def naslovna_stran():
    return bottle.template(pot("naslovnica.tpl"))


@bottle.post('/ustvarjanje_igre/')
def iniciiranje_igre():
    testni_seznam.clear()  # izbrišemo prejšnjo igro
    # pozor: tukaj ne moremo napisati kar testni_seznam = [], ker je potem to nova, lokalna spremenljivka. Globalna se torej ne spremeni.
    
    # nivo = model.Nivo([["", "", ""], ["", "z", ""], ["", "", "-s"]], (0, 0), [(2, 2), (1, 1)])
    nivo = model.Nivo([["", "", "", "", ""], ["-v", "s", "!", "", "!"], ["-s", "z", "", "", ""], ["", "!", "-j", "!", "-s"], ["", "", "", "", ""]], (0, 3), [(0, 2), (1, 2)])  # level 10 Boxup
    testni_seznam.append(nivo)
    bottle.redirect('/dejanska_igra/')

@bottle.get('/dejanska_igra/')
def igranje():
    # igra = testni_seznam[0]
    return bottle.template(pot("igrica.tpl"), game=testni_seznam[0])

@bottle.post('/dejanska_igra/')
def poteza():
    smer1 = bottle.request.forms.getunicode('smer')
    smer1 = smer1.lower()
    testni_seznam[0].premik_v_smer(smer1)
    bottle.redirect('/dejanska_igra/')

@bottle.get('/testne_slike/<picture>')  # tu je lahko / na konc al pa ne
def serve_pictures(picture):
    return bottle.static_file(picture, root="UVP\\Projektna-naloga\\testne_slike")
# tukaj parametra ne moremo spremeniti v kaj drugega kot picture


bottle.run(reloader=True, debug=True)