% from barve import bar, slovar_velikosti
% rebase('UVP\\Projektna-naloga\\views\\osnova.tpl', title="Naslov")



    <!--

    <blockquote>
      Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
      <small>Študentje</small>
    </blockquote>
    -->


    <!-- V komentih se bodo dvojni {} tudi prebrali kot python koda (čeprav se ne bodo izvedli). Zato jih je treba odstraniti tudi iz komentov-->
    % # lahko pa tako: {{asdfghjk}}
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
    <!-- Narisat je treba game -->
    % sez = game.matrika_z_igralcem().seznam_seznamov
    Število opravljenih potez: {{game.št_potez}}
    <table style="border:1px solid black; border-collapse:collapse; width:100%; height:80%;">
      % for vrstica in sez:
        <tr>
          % for člen in vrstica:
            <td>
              % counter = 0
              % if člen == "":
                <div style="position: relative; top: 0; left: 0; text-align: center;">
                  <img src="/Projektna-naloga/slike/praznina.png" alt="Slike ni na tem naslovu!" class="spodnji"/>
                </div>
                % continue
              % end
              <div style="position: relative; top: 0; left: 0; text-align: center;">
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

                  <!-- <img src="/slike/{{povezava}}.png" alt="Slike ni na tem naslovu!" class="razred_{{ime_razreda}}"></img>  -->
                  % if counter == 1:  # counter je vedno vsaj 1. Če je 1, je to spodnja slika, če več, je nespodnja
                    % ime_razreda = "spodnji"
                  % elif counter >= 2:
                    % ime_razreda = "nespodnji"
                  % end
                  <img src="/Projektna-naloga/slike/{{št_velikosti}}/{{povezava}}.png" alt="Slike ni na tem naslovu!" class="{{ime_razreda}}"></img>
          
                % end
              </div>
    
              <!-- <img src="/slike/{povezava}.png" alt="Slike ni na tem naslovu!" style="width:50%"></img>        Izgleda, da spreminjanje širine ohranja razmerje višine in širine, spreminjanje višine pa ne-->
            </td>
          % end
        </tr>
      % end
    </table>
    <!--
      <img src="../Projektna-naloga/slike/ime.jpg" alt="1"></img>    ne dela, saj link tukaj pomeni link do spletne strani, ne pa file explorer. Drugače bi imeli \\ med "folderji"
      <img src="/../ime.jpg/" alt="2"></img>     ne dela 
      <img src="../ime.jpg/" alt="3"></img>     ne dela 
      <img src="/ime.jpg" alt="4"></img>    ne dela 
      <img src="ime.jpg" alt="5"></img>    ne dela 
      <img src="/ime.jpg/" alt="6"></img>    ne dela 
      <img src="ime.jpg/" alt="7"></img>    ne dela 
      <img src="slike/ime.jpg" alt="8"></img>    ne dela (vse naprej delajo)
      <img src="/slike/ime.jpg" alt="9"></img>
      <img src="../slike/ime.jpg" alt="10"></img>
      <img src="/../slike/ime.jpg" alt="11"></img>
      <img src="../../slike/ime.jpg" alt="12"></img>

      Na koncu linka je zmeraj /slike/ime.jpg, namreč tako smo določili v spletni_vmesnik.py. 
      Pikice izgleda da ne morejo škoditi: to samo doda starševsko mapo, če pač slika ne bi bila v naši mapi (trenutno smo se mi zdi v mapi slike). Slika bi lahko bila kje drugje kot v mapi slike, zato pač moramo najprej iti v kakšno bolj zgornjo mapo.
      To, ali na koncu dodamo še eno poševnico, ne spremeni ničesar. Oba zapisa sta v redu.
    -->
    
    % if napaka is not None:
    <div class="row">
      <div class="{{opozorilna_barva}} z-depth-1 card-panel">
        <p>
      % if napaka[0] == "smer":
        Vnos {{napaka[1]}} ni veljaven!
      % end
        </p>
      </div>
    </div>
    % end


    % if game.preveri_ali_na_cilju():
    <div class="row">
      <div class="{{default_barva}} z-depth-1 card-panel"><h1>ZMAGA!</h1></div>
    </div>
      % if ime.isdigit():
        % if int(ime) < max_stevilo:
          <form action="/Level_n/{{int(ime) + 1}}/" method="post">
            <button class="{{tip}}" type="submit">
              Naslednji nivo
            </button>
          </form>
        % else:
          To je bil zadnji uradni nivo. Lahko pa poskusite katerega izmed tistih, ki so jih oblikovali uporabniki.
        % end
        % # za custom nivoji ni naslednjega nivoja
      % end

    % else:

    <form class="col s12" action="/dejanska_igra/" method="post">
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

    <form action="/Level_n/{{ime}}/" method="post">
      <div class="col s12">
      <button class="{{tip}}" type="submit">
        Ponastavi nivo
      </button>
    </div>
    </form>

    % end

    <form action="/seznam_levelov/" method="get">
      <div class="col s12">
        <button class="{{tip}}" type="submit">
          Seznam levelov
        </button>
      </div>
    </form>


