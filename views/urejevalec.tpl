% from barve import bar, slovar_velikosti
% rebase(povezava_za_bazo, title="Naslov")

% default_barva = "blue lighten-3"  # lahko tudi "light-green accent-2"
% opozorilna_barva = "red lighten-3"

% tip = "waves-effect waves-yellow btn"
% # https://bottlepy.org/docs/dev/stpl.html za znake kot so % ipd
% št_velikosti = igra.velikostna_stopnja
% alt_sporočilo = "Premajhna_velikost_levela"

<!-- Narišemo matriko -->
% sez = igra.matrika_z_igralcem().seznam_seznamov
<table style="border:1px solid black; border-collapse:collapse; width:100%">
  % for y, vrstica in enumerate(sez):
    <tr>
      % for x, člen in enumerate(vrstica):
        <td style="height:120px">
          % counter = 0
          <div style="position: relative; top: 0; left: 0; text-align: center;">
            
            <form action="/urejevalec/koord{{x}}-{{y}}/" method="post">

              % if člen == "":
                <button class="osnovni" type="submit"><img src="/Projektna-naloga/slike/praznina.png" alt={{alt_sporočilo}}/></button>
                </form>  <!-- Končamo form in div in pa stolpec, saj smo predčasno zapustili zanko -->
                </div>
                </td>
                % continue
              % end

              % for indeks, znak in enumerate(člen):
                % povezava = "skatla"
                % barva = "crna"
                % if znak == "-":
                  % continue
                % elif znak == "+":
                  % povezava = "igralec"
                % elif znak == "!":
                  % povezava = "skala"
                  % # izriši škatlo
                % else:
                  % if znak.lower() != znak:  # če znak vlka črka
                    % barva = bar[slovar_velikosti[str(indeks + 1)]]
                  % end
                  % povezava += str(indeks + 1) + znak.lower() + "_" + barva
                % end
                % counter += 1
                % povezava += str(št_velikosti)  # dodamo "velikostni razred trenutnega levela"
              % end

              <button class="osnovni" type="submit"><img src="/Projektna-naloga/slike/{{št_velikosti}}/{{povezava}}.png" alt={{alt_sporočilo}}/></button>
            </form>
          </div>
        </td>
      % end
    </tr>
  % end
</table>

<div class="divider"></div>

% seznam = ["+", "-", "!"]

% for i in range(št_velikosti):
  % seznam.append(i * "-" + "w")
  % seznam.append(i * "-" + "W")
% end

% seznam += ["puscica1", "puscica2"]
% dolžina_vrste = 6
% nov_seznam = []

% for i in range((len(seznam) - 1) // dolžina_vrste + 1):
  % nov_seznam.append(seznam[i * dolžina_vrste:(i + 1) * dolžina_vrste])
% end

% for i in range((-len(seznam)) % dolžina_vrste):
  % nov_seznam[-1].append(None)
% end

<table style="border:1px solid black; border-collapse:collapse; width:100%">
  % for sez in nov_seznam:
    <tr>
      % for niz in sez:
        <td style="height:120px">
          
          % if niz is None:  # to je zato, da izpolnemo tabelo do konca
            </td>  <!-- Končamo stolpec, saj smo predčasno zapustili zanko -->
            % continue
          % end

          % razred = "osnovni"

          % if niz == izbran_objekt:
            % razred = "poudarjen"
          % end

          <div style="position: relative; top: 0; left: 0; text-align: center;">
            <form action="/urejevalec/{{niz}}/" method="post">

              % if niz == "-":
                <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/praznina.png" alt={{alt_sporočilo}}/></button>
                </form>  <!-- Končamo form, div in pa stolpec, saj smo predčasno zapustili zanko -->
                </div>
                </td>
                % continue
              % end

              % for indeks, znak in enumerate(niz):
                % povezava = "skatla"
                % barva = "crna"

                % if znak == "-":
                  % continue
                % elif znak == "+":
                  % povezava = "igralec"
                % elif znak == "!":
                  % povezava = "skala"
                  % # izriši škatlo
                % else:
                  % if znak.lower() != znak:  # če znak vlka črka
                    % barva = bar[slovar_velikosti[str(indeks + 1)]]
                  % end
                  % povezava += str(indeks + 1) + znak.lower() + "_" + barva
                % end

                % povezava += str(št_velikosti)  # dodamo "velikostni razred trenutnega levela"

                % if niz == "puscica1": # itak samo enkrat na zanko pride do sem
                  <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/puscica+.png" alt={{alt_sporočilo}}/></button>
                  % break
                % elif niz == "puscica2":
                  <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/puscica-.png" alt={{alt_sporočilo}}/></button>
                  % break
                % else:
                  <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/{{št_velikosti}}/{{povezava}}.png" alt={{alt_sporočilo}}/></button>
                % end
              % end
            </form>
          </div>
        </td>
      % end
    </tr>
  % end
</table>

% if napaka is not None:
  <div class="row">
    <div class="{{opozorilna_barva}} z-depth-1 card-panel col s6">
      <p>
        % if napaka[0] == "ime":
          Ime {{napaka[1]}} ni ustrezno!
        % elif napaka[0] == "škatla":
          Ne moreta biti manj kot dve barvni škatli naenkrat v nivoju!
        % elif napaka[0] == "nivo":
          Nivo z imenom {{napaka[1]}} je že v bazi nivojev!
        % elif napaka[0] == "igralec":
          Ne morete izbrisati igralca!
        % elif napaka[0] == "polje":
          To polje je že zasedeno
        % elif napaka[0] == "rotacija":
          Ne morete rotirati objektov, ki niso škatle!  
        % end
      </p>
    </div>
  </div>
% end    

<div class="row">
  <div class="{{default_barva}} z-depth-1 card-panel col s8">
    <h5>
      Trenutno ime nivoja:
    </h5> 
  </div>
  <div class="{{default_barva}} z-depth-1 card-panel col s3 offset-s1">
    <p>
      {{ime}}
    </p>
  </div>
</div>

<form action="/urejevalec/" method="post">
  <div class="row">
    <div class="input-field col s6">
      <label >Zamenjajte ime nivoja: </label>
      <input type="text" name='ime' placeholder="Novo ime">
    </div>
    <button class="{{tip}}" type="submit">Zamenjajte ime</button>
  </div>
</form>

<form action="/urejevalec/" method="post">

  <div class="row">
    <div class="input-field col s6">
      <select name= "stopnja">
        % for i in range(2, 4):
          % if i == št_velikosti:
            <option value="{{i}}" selected>{{i}}</option>
          % else:
            <option value="{{i}}">{{i}}</option>
          % end
        % end
      </select>
      <label>Velikost:</label>
    </div>   
    <button class="{{tip}}" type="submit">Zamenjajte število velikosti</button>
  </div>
  <script>
    $(document).ready(function() {
      $('select').material_select();
    });
  </script>
  
</form>


<div class="divider"></div>

<form action="/shrani_nivo/" method="post">
  <button class="{{tip}}" type="submit">Shranite nivo</button>
</form>

<form action="/pridobi_seznam/" method="post">
  <button class="{{tip}}" type="submit">Nazaj na seznam nivojev</button>
</form>