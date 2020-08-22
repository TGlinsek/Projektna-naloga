% from barve import bar, slovar_velikosti
% rebase(povezava_za_bazo, title="Naslov")



% default_barva = "blue lighten-3"  # lahko tudi "light-green accent-2"
% opozorilna_barva = "red lighten-3"
% obvestilna_barva = "yellow lighten-4"
% tip = "waves-effect waves-yellow btn"
% # https://bottlepy.org/docs/dev/stpl.html za znake kot so % ipd
% št_velikosti = igra.velikostna_stopnja

<!-- Poskrbimo za rekorde -->
% svetovni_rekord = nivoji[ime][1]
% pomožni_slovar = {}
% for i, poteze in reseni_nivoji:
  % pomožni_slovar[i] = poteze
% end

% nivo_dokončan = ime in pomožni_slovar.keys()
% uporabnikov_rekord = pomožni_slovar[ime] if nivo_dokončan else "Ni še dokončano!"

<!--
% sez = igra.matrika_z_igralcem().seznam_seznamov
<div class="row">
  <div class="{{default_barva}} z-depth-1 card-panel col s3">
    <p>
      Število opravljenih potez: {{igra.št_potez}}
    </p>
  </div>
</div> -->
<div style="width: 50%; display: inline-block;">Število opravljenih potez: {{igra.št_potez}}</div>
<div style="width: 49%; display: inline-block; text-align: right;">Ime nivoja: {{ime}}</div>

<!-- Narisati je treba igro: -->
<table style="border:1px solid black; border-collapse:collapse; width:100%; height:80%;">
  % for vrstica in sez:
    <tr style="border: solid 1px; border-style: dotted;">
      % for člen in vrstica:
        <td style="border: solid 1px; border-style: dotted;">
          % counter = 0
          <div style="position: relative; top: 0; left: 0; text-align: center;">

            % if člen == "":
              <img src="/Projektna-naloga/slike/praznina.png" alt="Slike ni na tem naslovu!" class="spodnji"/>
              </div>  <!-- Ker sledi ukaz "continue", moramo zaključiti trenutne elemente (div in td) -->
              </td>
              % continue
            % end

            % for indeks, znak in enumerate(člen):
              % povezava = "skatla"
              % barva = "crna"
              % ime_razreda = ""
              % if znak == "-":
                % continue
              % elif znak == "+":
                % povezava = "igralec"
                % ime_razreda = "igralec"
              % elif znak == "!":
                % povezava = "skala"
                % ime_razreda = "skala"
                % # izriši škatlo
              % else:
                % if znak.lower() != znak:  # če znak vlka črka
                  % barva = bar[slovar_velikosti[str(indeks + 1)]]
                % end
                % povezava += str(indeks + 1) + znak.lower() + "_" + barva
                % ime_razreda = str(indeks + 1)
              % end
              % counter += 1
              % povezava += str(št_velikosti)  # dodamo "velikostni razred trenutnega levela"

              % if counter == 1:  # counter je vedno vsaj 1. Če je 1, je to spodnja slika, če več, je nespodnja
                % ime_razreda = "spodnji"
              % elif counter >= 2:
                % ime_razreda = "nespodnji"
              % end
              
              <img src="/Projektna-naloga/slike/{{št_velikosti}}/{{povezava}}.png" alt="Slike ni na tem naslovu!" class="{{ime_razreda}}"></img>
            % end
          </div>
        </td>
      % end
    </tr>
  % end
</table>

% if napaka is not None:
<div class="row">
  % ime_napake = napaka[0]
  % vsebina_napake = napaka[1]
  % if ime_napake == "smer":
  <div class="{{opozorilna_barva}} z-depth-1 card-panel col s12">
    <p>
      Vnos "{{vsebina_napake}}"" ni veljaven!
    </p>
  </div>
  % end

  % if ime_napake == "rekord":
  <div class="{{default_barva}} z-depth-1 card-panel col s12">
    <h5>
      Čestitke!
    </h5>
  </div>
  <div class="{{default_barva}} z-depth-1 card-panel col s4 offset-s4">
    <p>
      % if vsebina_napake is None:
        Izenačili ste dosedanji rekord!
      % elif vsebina_napake:
        % if napaka[2] == float("inf"):
          Prvi ste dokončali ta nivo!
        % else:
            % sporočilo = "Podrli ste dosedanji rekord! Prejšnji rekord je bil " + str(napaka[2])
            % if napaka[4] != float("inf"):
              % if napaka[4] == napaka[2]:
                % sporočilo += ", kot tudi vaš osebni rekord."
              % else:
                % sporočilo += ", vaš osebni rekord pa je bil" + str(napaka[4])
              % end
            % else:
              % sporočilo += "."
            % end
            {{sporočilo}}
        % end
      % elif napaka[3] is None:
        Izenačili ste osebni rekord!
      % elif napaka[3] and napaka[4] != float("inf"):
        Podrli ste osebni rekord! Prejšnji osebni rekord je bil {{napaka[4]}}.
      % else:
        Uspelo vam je!
      % end
    </p>
  </div>
  % end
</div>
% end


% if igra.preveri_ali_na_cilju():
  % if ime.isdigit():
    % if int(ime) < max_stevilo:
      <form action="/nalaganje_nivoja/{{int(ime) + 1}}/" method="post">
        <button class="{{tip}}" type="submit">
          Naslednji nivo
        </button>
      </form>
    % else:
      <div class="row">
        <div class="{{obvestilna_barva}} z-depth-1 card-panel col s12">
          <p>
            To je bil zadnji uradni nivo. Lahko pa poskusite katerega izmed tistih, ki so jih oblikovali uporabniki.
          </p>
        </div>
      </div>
    % end
    % # za custom nivoji ni naslednjega nivoja
  % end

% else:
  <form class="col s12" action="/igra/" method="post">
    <div class="row">
      <div class="input-field col s12">
        <label >Vnesi črko:</label>
        <input type="text" placeholder="w, a, s, d" name='smer' autofocus>
        <button class="{{tip}}" type="submit">
          Pošlji ukaz
        </button>
      </div>
    </div>
  </form>

  <form action="/nalaganje_nivoja/{{ime}}/" method="post">
    <div class="col s12">
      <button class="{{tip}}" type="submit">
        Ponastavi nivo
      </button>
    </div>
  </form>

% end
<div class="divider"></div>

<div class="row">
  <div class="{{default_barva}} z-depth-1 card-panel col s8"><h6>Osebni rekord: {{uporabnikov_rekord}}</h6></div>
  <div class="{{default_barva}} z-depth-1 card-panel col s3 offset-s1"><h6>Svetovni rekord: {{svetovni_rekord if svetovni_rekord != float("inf") else "Nihče še ni dokončal nivoja!"}}</h6></div>
</div>

<form action="/pridobi_seznam/" method="post">
  <div class="col s12">
    <button class="{{tip}}" type="submit">
      Seznam levelov
    </button>
  </div>
</form>


