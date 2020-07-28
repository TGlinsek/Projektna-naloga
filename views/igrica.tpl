<!DOCTYPE html>
<html>

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

    <!-- Narisat je treba game -->
    % sez = game.matrika_z_igralcem().seznam_seznamov
    <table style="border:1px solid black; border-collapse: collapse">
      % for i in sez:
        <tr>
          % for j in i:
            <td>
              {{j if j != "" else "-"}}
            </td>
          % end
        </tr>
      % end
    </table>

    % # lahko bi napisali tudi {{game}}, ampak potem izriše matriko v eno samo vrstico

    % if game.preveri_ali_na_cilju():

    <h1>ZMAGA!</h1>
    <form action="/ustvarjanje_igre/" method="post">
      <button type="submit">Nova igra</button>
    </form>

    % else:

    <form action="/dejanska_igra/" method="post">
      Črka: <input type="text" name='smer' autofocus>
      <button type="submit">Pošlji ugib</button>
    </form>

    % end

  </body>

</html>