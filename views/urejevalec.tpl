% from barve import bar, slovar_velikosti
<!DOCTYPE html>
<html>
  <head>
    <style>
      .spodnji {
        width: 50%;
      }
      .spodnji:hover {
        width: 50%;
        background: rgba(0,0,0,.3);
      }
      .poudarjen {
        width: 50%;
        background: rgba(0,0,0,.2);
      }
      .poudarjen:hover {
        width: 50%;
        background: rgba(0,0,0,.5);
      }
    </style>
  </head>

  <body>

    <h1>Igra</h1>

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
    % # https://bottlepy.org/docs/dev/stpl.html za znake kot so % ipd
    % št_velikosti = game.velikostna_stopnja
    <!-- Narisat je treba game -->
    % sez = game.matrika_z_igralcem().seznam_seznamov
    <table style="border:1px solid black; border-collapse:collapse; width:100%">
      % for y, vrstica in enumerate(sez):
        <tr>
          % for x, člen in enumerate(vrstica):
            <td style="height:120px">
              % counter = 0
              % if člen == "":
                <div style="position: relative; top: 0; left: 0">
                  <form action="/urejevalec/koord{{x}}-{{y}}/" method="post">
                    <button class="spodnji" type="submit"><img src="/Projektna-naloga/testne_slike/praznina.png" alt="Slike ni na tem naslovu!"/></button>
                  </form>
                </div>
                % continue
              % end
              <div style="position: relative; top: 0; left: 0">
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
                    <button class="spodnji" type="submit"><img src="/Projektna-naloga/testne_slike/{{št_velikosti}}/{{povezava}}.png" alt="Slike ni na tem naslovu!"/></button>
                  </form>
                % end
              </div>
            </td>
          % end
        </tr>
      % end
    </table>






      <!-- <input type="image" src="/Projektna-naloga/testne_slike/2/igralec2.png" /> -->
      <!-- https://stackoverflow.com/questions/8683528/embed-image-in-a-button-element -->


    % # bar[slovar_velikosti["1"]] --> rdeca
    % # začnemo z "1", končamo z besedo
    % seznam = ["+", "-", "!"]
    % for i in range(št_velikosti):
    %   seznam.append(i * "-" + "s")
    %   seznam.append(i * "-" + "S")
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
          % razred = "spodnji"
          % if niz == izbran_objekt:
            % razred = "poudarjen"
          % end
          % if niz is None:  # to je zato, da izpolnemo tabelo do konca
            % continue
          % end
          % if niz == "-":
            <div style="position: relative; top: 0; left: 0">
              <form action="/urejevalec/{{niz}}/" method="post">
                <button class={{razred}} type="submit"><img src="/Projektna-naloga/testne_slike/praznina.png" alt="Slike ni na tem naslovu!"/></button>
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
            <div style="position: relative; top: 0; left: 0">
              % if niz == "puscica1": # itak samo enkrat na zanko pride do sem
                <form action="/urejevalec/puscica1/" method="post">
                  <button class={{razred}} type="submit"><img src="/Projektna-naloga/testne_slike/puscica+.png" alt="Slike ni na tem naslovu!"/></button>
                </form>
                % break
              % elif niz == "puscica2":
                <form action="/urejevalec/puscica2/" method="post">
                  <button class={{razred}} type="submit"><img src="/Projektna-naloga/testne_slike/puscica-.png" alt="Slike ni na tem naslovu!"/></button>
                </form>
                % break
              % else:
                <form action="/urejevalec/{{niz}}/" method="post">
                  <button class={{razred}} type="submit"><img src="/Projektna-naloga/testne_slike/{{št_velikosti}}/{{povezava}}.png" alt="Slike ni na tem naslovu!"/></button>
                </form>
              % end
            </div>
          % end
        </td>
        % end
      </tr>
      % end
    </table>

    Trenutno ime nivoja: {{ime}}
    <form action="/urejevalec/" method="post">
      Novo ime nivoja: <input type="text" name='ime' autofocus>
      <button type="submit">Zamenjaj ime</button>
    </form>

    <form action="/shrani_nivo/" method="post">
      <button type="submit">Shrani nivo</button>
    </form>

    <form action="/seznam_levelov/" method="get">
      <button type="submit">Nazaj na seznam nivojev</button>
    </form>

    <form action="/urejevalec/" method="post">
      <label>Velikostna stopnja:</label>
      <select name= "stopnja">
        % for i in range(2, 4):
          <option value="{{i}}">{{i}}</option>
        % end
      </select>
      <button type="submit">Zamenjaj število velikostnih stopenj v nivoju</button>
    </form>
    % # if len(game.slovar_barvnih_škatel) < 2: error
    % if napaka is not None:
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
    % end
  </body>

</html>