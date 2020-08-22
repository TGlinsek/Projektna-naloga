% rebase(povezava_za_bazo, title="Naslov")
% tip = "waves-effect waves-yellow btn"  # tip gumba
<h1>Nivoji</h1>

<table style="width:100%;">
  <tr>
    <th>Ime nivoja</th>
    <th>Že dokončan?</th>
    <th>Osebni rekord</th>
    <th>Rekord</th>
    <th>Igraj</th>
    <th>Uredi</th>
  </tr>

  % pomožni_slovar = {}
  % for ime, poteze in reseni_nivoji:
    % pomožni_slovar[ime] = poteze
  % end

  % for lvl in vsi_nivoji.keys():
  <tr style="border: 1px solid black;">
    <td>{{lvl}}</td>
    % nivo_dokončan = lvl in pomožni_slovar.keys()
    <td>{{"Da" if nivo_dokončan else "Ne"}}</td>
    <td>{{pomožni_slovar[lvl] if nivo_dokončan else "Nedefinirano"}}</td>
    % št_potez = vsi_nivoji[lvl][1]
    <td>{{"Nihče še ni dokončal" if št_potez == float("inf") else št_potez}}</td>
    <td>
      <form action="/nalaganje_nivoja/{{lvl}}/" method="post">
        <button class="{{tip}}" type="submit">Igraj</button>
      </form>
    </td>
    <td>
      <form action="/urejanje_nivoja/{{lvl}}/" method="post">
        <button class="{{tip}}" type="submit">Urejanje</button>
      </form>
    </td>
  </tr>
  % end
</table>
<form action="/nazaj_na_prvo_stran/" method="post">
  <button class="{{tip}}" type="submit">Glavni menu</button>
</form>
