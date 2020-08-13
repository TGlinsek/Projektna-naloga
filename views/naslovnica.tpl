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


    <!-- 
    <img src="img/10.jpg" alt="obesanje">
    -->

    <form action="/Level_n/1/" method="post">
      <button type="submit">Nova igra</button>
    </form>

    <form action="/seznam_levelov/" method="get">
      <button type="submit">Seznam nivojev</button>
    </form>

    Lahko tudi ustvariš svoj nivo:
    <form action="/Level_n_urejanje/" method="post">
      <label>Širina:</label>
      <select name= "sirina">
        % for i in range(3, 8):
          <option value="{{i}}" >{{i}}</option>
        % end
      </select>
      <label>Višina:</label>
      <select name= "visina">
        % for i in range(3, 8):
          <option value="{{i}}" >{{i}}</option>
        % end
      </select>
      <button type="submit">Ustvari svoj nivo</button>
    </form>
  
  </body>

</html>