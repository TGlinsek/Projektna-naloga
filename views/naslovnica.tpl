% rebase(povezava_za_bazo, title="Naslov")
% tip = "waves-effect waves-yellow btn"
% default_barva = "blue lighten-3"  # lahko tudi "light-green accent-2"

% if prvi_obisk:
  Dobrodošli!
% else:
  Dobrodošli nazaj!
% end

<form action="/nalaganje/" method="post">
  <div class="col s12">
    <button class="{{tip}}" type="submit">
      Start
    </button>
  </div>
</form>
