# izriše dve sliki ukrivljenih puščic v datoteki "puscica-.png" in "puscica+.png", kjer - in + označujeta orientacijo puščic
from PIL import Image, ImageDraw
import os
import math

from pathlib import Path


cwd = os.getcwd()
starš = Path(__file__).parent

os.chdir(starš)

os.chdir("slike")

def shrani(destinacija, slika):  # brez končnice
    pot = destinacija + ".png"
    slika.save(pot)

def sind(angle):
    return math.sin(math.radians(angle))

def cosd(angle):
    return math.cos(math.radians(angle))

def koordinate_črt(kot, kot_črt, dolžina_črt, konica, predznak):  # vrne nabor dveh točk
    prva_konica = (konica[0] + cosd(kot - kot_črt - predznak * kotni_popravek) * dolžina_črt, konica[1] + sind(kot - kot_črt - predznak * kotni_popravek) * dolžina_črt)
    druga_konica = (konica[0] + cosd(kot + kot_črt - predznak * kotni_popravek) * dolžina_črt, konica[1] + sind(kot + kot_črt - predznak * kotni_popravek) * dolžina_črt)
    return (prva_konica, druga_konica)
    # predznak je samo popravek za kot


barva_črt = (0, 0, 0)

dimenzija = 100

debelina = 5

out = Image.new("RGBA", (dimenzija, dimenzija), (255, 0, 0, 0))  # A na koncu kratice RGBA označuje alfo (transparentnost)
draw = ImageDraw.Draw(out, mode="RGBA")

polmer = 40  # polmer krožnice, na kateri teče puščica

kot_črt = 30  # lahko spreminjaš (ampak boš mogoče moral spremeniti tudi popravek)
dolžina_črt = 20  # dolžina krakov

kot_loka = -150  # kot ukrivljenega dela puščice

kot = kot_loka + 90  # to je samo za usmerjenje krakov puščice

# popravek zaradi iluzije, kjer kraki puščice ne izgledajo centrirani zaradi ukrivljanja puščice
kotni_popravek = 19  # za kot -150 izgleda 19 kar dober popravek

konica = (dimenzija / 2 + polmer * cosd(kot_loka), dimenzija / 2 + polmer * sind(kot_loka))  # koordinate konice puščice    

prva_konica, druga_konica = koordinate_črt(kot, kot_črt, dolžina_črt, konica, -1)  # koordinate obeh koncev krakov

# ta spremenljivka bo enaka za obe sliki (se ne spreminja)
okvir = ((dimenzija / 2 - polmer, dimenzija / 2 - polmer), (dimenzija / 2 + polmer, dimenzija / 2 + polmer))  # koordinate leve zgornje točke in desne spodnje točke okvirja, v katerem leži krožnica za puščico

draw.arc(okvir, kot_loka, -kot_loka, fill=barva_črt, width=debelina)  # nariši lok

draw.line((konica, prva_konica), fill=barva_črt, width=debelina)  # prvi krak
draw.line((konica, druga_konica), fill=barva_črt, width=debelina)  # drugi krak

ime = "puscica+"
shrani(ime, out)



kot_loka = -kot_loka  # zrcaljenje

out = Image.new("RGBA", (dimenzija, dimenzija), (255, 0, 0, 0))
draw = ImageDraw.Draw(out, mode="RGBA")

kot = 180 - kot  # suplementarni kot, zaradi zrcaljenja slike
konica = (dimenzija / 2 - polmer * cosd(kot_loka), dimenzija / 2 - polmer * sind(kot_loka))  # konica se tudi zrcali

prva_konica, druga_konica = koordinate_črt(kot, kot_črt, dolžina_črt, konica, 1)  # 1 je samo popravek za kot
draw.arc(okvir, 180 - kot_loka, kot_loka - 180, fill=barva_črt, width=debelina)

draw.line((konica, prva_konica), fill=barva_črt, width=debelina)
draw.line((konica, druga_konica), fill=barva_črt, width=debelina)

ime = "puscica-"
shrani(ime, out)