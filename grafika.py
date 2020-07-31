from PIL import Image, ImageDraw
import os
# Inštalacija: v cmd napišemo python -m pip install Pillow


št_velikosti = 2  # 2 je default, lahko je tudi več
št_pikslov = št_velikosti * 4 + 6  # to je sam na kok delov moramo razdelit sliko. Slika bo torej toliko na kvadrat


# image1 = Image.open("UVP\\Projektna-naloga\\Prazno.png")  
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html


# tako začnemo risati:
"""
out = Image.new("RGBA", (100, 100), (255, 0, 0, 0))  # transparentno
draw = ImageDraw.Draw(out, mode="RGBA")  # mode od Image in od ImageDraw mora biti isti
"""

# črta:
# draw.line((0, out.size[0], out.size[1], 20), fill=128)  # x1, y1, x2, y2


os.chdir("UVP")  # pojdi v mapo UVP
os.chdir("Projektna-naloga")
os.chdir("testne_slike")  # ustvarimo novo mapo z imenom testne_slike, kamor se bodo slike shranjevale


barve = {(255, 0, 0): "rdeča", (0, 0, 255): "modra", (0, 0, 0): "črna"}

smeri = {"s", "j", "v", "z"}


def shrani(destinacija, slika):  # brez končnice
    pot = destinacija + ".png"
    slika.save(pot)


def izriši_pravokotnik(draw, koordinate_1, koordinate_2, barva):  # celoštevilske koordinate pretvorimo v dejanske (od 0 do 100)
    nove_koordinate_1 = (100 * koordinate_1[0] / št_pikslov, 100 * koordinate_1[1] / št_pikslov)
    nove_koordinate_2 = (100 * koordinate_2[0] / št_pikslov, 100 * koordinate_2[1] / št_pikslov)
    draw.rectangle((nove_koordinate_1, nove_koordinate_2), fill=barva)


def izriši_sliko(velikost, smer, barva):
    out = Image.new("RGBA", (100, 100), (255, 0, 0, 0))
    draw = ImageDraw.Draw(out, mode="RGBA")
    
    indeks = št_velikosti - velikost  # 0 je za najbolj zunanje, potem je 1, itd.
    premik = 2 * indeks  # za vsako spremembo velikosti je treba za dva "piksla" vse skupaj premakniti
    if smer != "s":
        koord1 = (1 + premik, 1 + premik)
        koord2 = (št_pikslov - 1 - premik, 2 + premik)
        izriši_pravokotnik(draw, koord1, koord2, barva)
    if smer != "j":
        koord1 = (1 + premik, št_pikslov - 2 - premik)
        koord2 = (št_pikslov - 1 - premik, št_pikslov - 1 - premik)
        izriši_pravokotnik(draw, koord1, koord2, barva)
    if smer != "v":
        koord1 = (št_pikslov - 2 - premik, 1 + premik)
        koord2 = (št_pikslov - 1 - premik, št_pikslov - 1 - premik)
        izriši_pravokotnik(draw, koord1, koord2, barva)
    if smer != "z":
        koord1 = (1 + premik, 1 + premik)
        koord2 = (2 + premik, št_pikslov - 1 - premik)
        izriši_pravokotnik(draw, koord1, koord2, barva)

    ime = "škatla" + str(velikost) + smer + "_" + barve[barva]
    shrani(ime, out)


def izriši_sliko_v_vse_smeri(velikost, barva):
    for smer in smeri:
        izriši_sliko(velikost, smer, barva)


slovar_velikosti = {"1": (255, 0, 0), "2": (0, 0, 255), "ostalo": (0, 0, 0)}  # ključi pomenijo barvo
for ključ in slovar_velikosti:
    barva = slovar_velikosti[ključ]
    if ključ == "ostalo":
        for i in range(1, št_velikosti + 1):
            izriši_sliko_v_vse_smeri(i, barva)
    else:
        izriši_sliko_v_vse_smeri(int(ključ), barva)

# igralec
out = Image.new("RGBA", (100, 100), (255, 0, 0, 0))
draw = ImageDraw.Draw(out, mode="RGBA")

koord1 = ((št_pikslov / 2) - 1, (št_pikslov / 2) - 1)
koord2 = ((št_pikslov / 2) + 1, (št_pikslov / 2) + 1)
        
izriši_pravokotnik(draw, koord1, koord2, (0, 0, 0))
ime = "igralec"
shrani(ime, out)




# skala
out = Image.new("RGBA", (100, 100), (255, 0, 0, 0))  # vsakič je treba posebej novo sliko narediti, drugače ne čečkamo po prazni sliki
draw = ImageDraw.Draw(out, mode="RGBA")

koord1 = (1, 1)
koord2 = (št_pikslov - 1, št_pikslov - 1)
        
izriši_pravokotnik(draw, koord1, koord2, (0, 0, 0))
ime = "skala"
shrani(ime, out)

# format izgleda takole:
# barva = (255, 0, 0)
# draw.rectangle(((25, 25), (50, 75)), fill=barva)


# za prikaz slike bi dali:
# out.show()