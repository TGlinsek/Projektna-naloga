% rebase(povezava_za_bazo, title="Naslov")
% tip = "waves-effect waves-yellow btn"
% default_barva = "blue lighten-3"  # lahko tudi "light-green accent-2"

<div class="{{default_barva}} z-depth-1 card-panel"><h4>Dobrodošli v igri Skladiščnik!</h4></div>

<form action="/nalaganje/" method="post">
  <div class="col s12">
    <button class="{{tip}}" type="submit">
      Začnite
    </button>
  </div>
</form>
