% from barve import bar, slovar_velikosti
% rebase('UVP\\Projektna-naloga\\views\\osnova.tpl', title="Naslov")



<!--

<blockquote>
  Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
  <small>Študentje</small>
</blockquote>
-->


<!-- V komentih se bodo dvojni {} tudi prebrali kot python koda (čeprav se ne bodo izvedli). Zato jih je treba odstraniti tudi iz komentov-->


<!-- 
<table>
<tr>
    <td>
    <h2>{igra.pravilni_del_gesla()}</h2>
    </td>
</tr>
<tr>
    <td>
    Nepravilni ugibi : {igra.nepravilni_ugibi()}
    </td>
</tr>
<tr>
    <td>
    <img src="../../img/{igra.stevilo_napak()}.jpg" alt="obesenec">
    Stopnja obešenosti : {igra.stevilo_napak()} / {model2.STEVILO_DOVOLJENIH_NAPAK + 1}
    </td>
</tr>
</table>
-->

% default_barva = "blue lighten-3"  # lahko tudi "light-green accent-2"
% opozorilna_barva = "red lighten-3"

% tip = "waves-effect waves-yellow btn"
% # https://bottlepy.org/docs/dev/stpl.html za znake kot so % ipd
% št_velikosti = game.velikostna_stopnja
% alt_sporočilo = "Premajhna_velikost_levela"
<!-- Narisat je treba game -->
% sez = game.matrika_z_igralcem().seznam_seznamov
<table style="border:1px solid black; border-collapse:collapse; width:100%">
  % for y, vrstica in enumerate(sez):
    <tr>
      % for x, člen in enumerate(vrstica):
        <td style="height:120px">
          % counter = 0
          % if člen == "":
            <div style="position: relative; top: 0; left: 0; text-align: center;">
              <form action="/urejevalec/koord{{x}}-{{y}}/" method="post">
                <button class="osnovni" type="submit"><img src="/Projektna-naloga/slike/praznina.png" alt={{alt_sporočilo}}/></button>
              </form>
            </div>
            % continue
          % end
          <div style="position: relative; top: 0; left: 0; text-align: center;">
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

              
              <form action="/urejevalec/koord{{x}}-{{y}}/" method="post">
                <button class="osnovni" type="submit"><img src="/Projektna-naloga/slike/{{št_velikosti}}/{{povezava}}.png" alt={{alt_sporočilo}}/></button>
              </form>
            % end
          </div>
        </td>
      % end
    </tr>
  % end
</table>


<div class="divider"></div>



  <!-- <input type="image" src="/Projektna-naloga/slike/2/igralec2.png" /> -->
  <!-- https://stackoverflow.com/questions/8683528/embed-image-in-a-button-element -->


% # bar[slovar_velikosti["1"]] --> rdeca
% # začnemo z "1", končamo z besedo
% seznam = ["+", "-", "!"]
% for i in range(št_velikosti):
%   seznam.append(i * "-" + "w")
%   seznam.append(i * "-" + "W")
% end
% seznam += ["puscica1", "puscica2"]
% dolžina_vrste = 5
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
      % razred = "osnovni"
      % if niz == izbran_objekt:
        % razred = "poudarjen"
      % end
      % if niz is None:  # to je zato, da izpolnemo tabelo do konca
        % continue
      % end
      % if niz == "-":
        <div style="position: relative; top: 0; left: 0; text-align: center;">
          <form action="/urejevalec/{{niz}}/" method="post">
            <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/praznina.png" alt={{alt_sporočilo}}/></button>
          </form>
        </div>
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
        <div style="position: relative; top: 0; left: 0; text-align: center;">
          % if niz == "puscica1": # itak samo enkrat na zanko pride do sem
            <form action="/urejevalec/puscica1/" method="post">
              <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/puscica+.png" alt={{alt_sporočilo}}/></button>
            </form>
            % break
          % elif niz == "puscica2":
            <form action="/urejevalec/puscica2/" method="post">
              <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/puscica-.png" alt={{alt_sporočilo}}/></button>
            </form>
            % break
          % else:
            <form action="/urejevalec/{{niz}}/" method="post">
              <button class={{razred}} type="submit"><img src="/Projektna-naloga/slike/{{št_velikosti}}/{{povezava}}.png" alt={{alt_sporočilo}}/></button>
            </form>
          % end
        </div>
      % end
    </td>
    % end
  </tr>
  % end
</table>


    % # if len(game.slovar_barvnih_škatel) < 2: error
    % if napaka is not None:
    <div class="row">
    <div class="{{opozorilna_barva}} z-depth-1 card-panel">
      <p>
      % if napaka[0] == "ime":
        Ime {{napaka[1]}} ni ustrezno!
      % elif napaka[0] == "škatla":
        Ne moreta biti manj kot dve barvni škatli!
      % elif napaka[0] == "nivo":
        Nivo z imenom {{napaka[1]}} je že v bazi nivojev!
      % elif napaka[0] == "igralec":
        Ne moreš izbrisati igralca!
      % elif napaka[0] == "polje":
        To polje je že zasedeno
      % elif napaka[0] == "rotacija":
        Ne moreš rotirati objektov, ki niso škatle!  
      % end
    </p>
  </div>
</div>
    % end    



  <div class="row">
    <div class="{{default_barva}} z-depth-1 card-panel"><h5>Trenutno ime nivoja:</h5> <p>{{ime}}</p></div>
  </div>

<form action="/urejevalec/" method="post">
  <div class="row">
    <div class="input-field col s6">
      <label >Zamenjaj ime nivoja: </label>
      <input type="text" name='ime' placeholder="Novo ime">
    </div>
    <button class="{{tip}}" type="submit">Zamenjaj ime</button>
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
      <label>Velikostna stopnja:</label>

    </div>   
    <button class="{{tip}}" type="submit">Zamenjaj število velikostnih stopenj v nivoju</button>
  
</div>
  <script>
   $(document).ready(function() {
     $('select').material_select();
   });
   </script>
  
</form>

<div class="divider"></div>

<form action="/shrani_nivo/" method="post">
  <button class="{{tip}}" type="submit">Shrani nivo</button>
</form>

<form action="/seznam_levelov/" method="get">
  <button class="{{tip}}" type="submit">Nazaj na seznam nivojev</button>
</form>


</form>