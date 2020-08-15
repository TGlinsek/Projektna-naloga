# Projektna-naloga
Miselna igra "Skladiščnik" predstavlja igralca - skladiščnika, ki v skladišču prelaga zaboje. Igralca predstavlja majhen črn kvadratek, nivo pa n x n tabelo, po kateri se igralec lahko premika s črkami "w", "a", "s" in "d", ki jih uporabnik vpiše v besedilno polje in igralca premaknejo gor, levo, dol ali desno, v tem vrstnem redu. Igralec se premakne le, če je to mogoče, torej, če ni napoti kakšna večja črna škatla (ki je igralec pod nobenim pogojem ne more premakniti), če igralec ne potiska zaboja iz zaprte strani ali pa če je igralec naletel na rob tabele. Zaboje lahko igralec potisne drug v drugega, če so velikosti ustrezne. Cilj igre je spraviti vse pobarvane zaboje (torej, ne črne) drug v drugega.

Načrt igre je navdihnjen po znani japonski miselni igri Sokoban, kjer igralec prav tako prelaga zaboje v skladišču.
Oštevilčeni nivoji so izposojeni iz https://www.mathsisfun.com/games/boxup-puzzle.html, ostali pa so originalni.

Za zagon programa poženite python datoteko skladiščnik.py, nato pa kliknite na povezavo, ki se prikaže v konzoli.
Prikaže se spletna stran, kjer lahko kliknete na gumb:
- "Nova igra", za začetek prvega nivoja,
- "Seznam nivojev", za ogled vseh nivojev,
- "Ustvari svoj nivo", če se želite preizkusiti v oblikovanju svojega nivoja. Pred tem lahko izberete dimenzije vašega nivoja.

Za premikanje igralca uporabnik pritisne gumb "Pošlji ukaz". Če se vam v igri zatakne, lahko ponastavite nivo s klikom na gumb "Ponastavi nivo".

Ko oblikujete nivo, najprej izberite objekt iz spodnje tabele, ki se bo s tem obarval. Nato pritisnite poljubno polje v tabeli, da izbran objekt postavite tja. Za izbris objekta najprej izberite prazno polje. Za rotiranje zabojev izberite puščico. Nivo lahko preimenujete s klikom na gumb "Zamenjaj ime". Če želite več različnih velikosti zabojev, jo lahko izberete iz spustnega menija in potrdite s klikom na gumb "Zamenjaj število velikosti". Ko ste končali z oblikovanjem, kliknite gumb "Shrani nivo". Nivo se bo potem dodal na seznam vseh nivojev. Ko nivo shranite, je viden vsem ostalim uporabnikom. Izbris nivoja ni možen.