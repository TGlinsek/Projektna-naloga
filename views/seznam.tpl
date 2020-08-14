% rebase('UVP\\Projektna-naloga\\views\\osnova.tpl', title="Naslov")
% tip = "waves-effect waves-yellow btn"
  <h1>Nivoji</h1>
  
  <table style="width:100%">
    <tr>
      <th>Ime nivoja</th>
      <th>Že zigran</th>
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
      % nivo_zigran = lvl in pomožni_slovar.keys()
      <td>{{"Da" if nivo_zigran else "Ne"}}</td>
      <td>{{pomožni_slovar[lvl] if nivo_zigran else "nedefinirano"}}</td>
      % št_potez = vsi_nivoji[lvl][1]
      <td>{{"Nihče še ni zigral" if št_potez == float("inf") else št_potez}}</td>
      <td>
        <form action="/Level_n/{{lvl}}/" method="post">
          <button class="{{tip}}" type="submit">Igraj</button>
        </form>
      </td>
      <td>
        <form action="/Level_n_urejanje/{{lvl}}/" method="post">
          <button class="{{tip}}" type="submit">Urejanje</button>
        </form>
      </td>
    </tr>
    % end
  </table>
  <form action="/dobrodošel/" method="get">
    <button class="{{tip}}" type="submit">Glavni menu</button>
  </form>
