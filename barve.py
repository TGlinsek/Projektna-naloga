# ta file uvažata grafika.py in igrica.tpl. 
# Vsebuje vse barve, ki se v vseh levelih skupaj pojavijo, 
# in največje število barvnih škatel, ki se v kateremkoli levelu pojavi

bar = {(255, 0, 0): "rdeca", (0, 0, 255): "modra", (0, 255, 0): "zelena", (0, 0, 0): "crna"}

# slovar naj ima vse možne barve, tudi če ne bodo vse uporabljene v vseh levelih. 
# Torej, tudi če je en sam level z maksimlano velikostjo 3, moramo dodati dodatno barvo
slovar_velikosti = {"1": (255, 0, 0), "2": (0, 0, 255), "3": (0, 255, 0), "ostalo": (0, 0, 0)}  # ključi pomenijo barvo
