<!DOCTYPE html>
<html>
  <head>
    <style>
      .spodnji {
        width: 50%;
        position: relative;
        top: 0;
        left: 0;
      }
      .nespodnji {
        width: 50%;
        position: absolute;
        top: 0;
        left: 0;
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
    % # https://bottlepy.org/docs/dev/stpl.html za znake kot so % ipd


    % # tole je vzeto iz grafika.py
    % barve = {(255, 0, 0): "rdeča", (0, 0, 255): "modra", (0, 0, 0): "črna"}
    % slovar_velikosti = {"1": (255, 0, 0), "2": (0, 0, 255), "ostalo": (0, 0, 0)}
    <!-- Narisat je treba game -->
    % sez = game.matrika_z_igralcem().seznam_seznamov
    <table style="border:1px solid black; border-collapse:collapse; width:100%">
      % for vrstica in sez:
        <tr>
          % for člen in vrstica:
            <td style="height:120px">
              % # {{člen if člen != "" else "-"}}
              % counter = 0
              <div style="position: relative; top: 0; left: 0">
                % for indeks, znak in enumerate(člen):
                  % povezava = "škatla"
                  % barva = "črna"
                  % ime_razreda = ""
                  % if znak == "-":
                    % continue
                  % elif znak == "+":
                    % povezava = "igralec"
                    % ime_razreda = "igralec"
                    % counter += 1
                  % elif znak == "!":
                    % povezava = "skala"
                    % ime_razreda = "skala"
                    % # izriši škatlo
                    % counter += 1
                  % else:
                    % if znak.lower() != znak:  # če znak vlka črka
                      % barva = barve[slovar_velikosti[str(indeks + 1)]]
                    % end
                    % povezava += str(indeks + 1) + znak.lower() + "_" + barva
                    % ime_razreda = str(indeks + 1)
                    % counter += 1
                  % end

                  <!-- <img src="/testne_slike/{{povezava}}.png" alt="Slike ni na tem naslovu!" class="razred_{{ime_razreda}}"></img>  -->
                  % if counter == 1:  # counter je vedno vsaj 1. Če je 1, je to spodnja slika, če več, je nespodnja
                    % ime_razreda = "spodnji"
                  % elif counter >= 2:
                    % ime_razreda = "nespodnji"
                  % end
                  <img src="/testne_slike/{{povezava}}.png" alt="Slike ni na tem naslovu!" class="{{ime_razreda}}"></img>
          
                % end
              </div>
    
              <!-- <img src="/testne_slike/{povezava}.png" alt="Slike ni na tem naslovu!" style="width:50%"></img>        Izgleda, da spreminjanje širine ohranja razmerje višine in širine, spreminjanje višine pa ne-->
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
    % # lahko bi napisali tudi {{game}}, ampak potem izriše matriko v eno samo vrstico

    % if game.preveri_ali_na_cilju():

    <h1>ZMAGA!</h1>
    <form action="/ustvarjanje_igre/" method="post">
      <button type="submit">Nova igra</button>
    </form>

    % else:

    <form action="/dejanska_igra/" method="post">
      Črka: <input type="text" name='smer' autofocus>
      <button type="submit">Pošlji ukaz</button>
    </form>

    % end

  </body>

</html>