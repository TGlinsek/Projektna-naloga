<!DOCTYPE html>
<html>

<body>

  <h1>Nivoji</h1>
  
  <table style="width:100%">
    <tr>
      <th>Ime nivoja</th>
      <th>Že zigran</th>
      <th>Igraj</th>
      <th>Uredi</th>
    </tr>
    % for lvl in vsi_nivoji:
    <tr>
      <td>{{lvl}}</td>
      <td>{{lvl in reseni_nivoji}}</td>
      <td>
        <form action="/Level_n/{{lvl}}/" method="post">
          <button type="submit">Igraj</button>
        </form>
      </td>
      <td>
        <form action="/Level_n_urejanje/{{lvl}}/" method="post">
          <button type="submit">Urejanje</button>
        </form>
      </td>
    </tr>
    % end
  </table>
</body>

</html>