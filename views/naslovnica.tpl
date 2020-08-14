% rebase('UVP\\Projektna-naloga\\views\\osnova.tpl', title="Naslov")
% tip = "waves-effect waves-yellow btn"
% default_barva = "blue lighten-3"  # lahko tudi "light-green accent-2"
    <form action="/Level_n/1/" method="post">
      <div class="col s12">
        <button class="{{tip}}" type="submit">
          Nova igra
        </button>
      </div>
    </form>

    <form action="/seznam_levelov/" method="get">
      <div class="col s12">
        <button class="{{tip}}" type="submit">
          Seznam nivojev
        </button>
      </div>
    </form>
    <div class="divider"></div>
    <div class="row">
      <div class="{{default_barva}} z-depth-1 card-panel"><h5>Lahko tudi ustvariš svoj nivo:</h5></div>
    </div>
    <form action="/Level_n_urejanje/" method="post">

      
      <div class="row">
        <div class="input-field col s6">

          <select name= "sirina">
            % for i in range(3, 8):
              % if i == 5:
                <option value="{{i}}" selected>{{i}}</option>
              % else:
                <option value="{{i}}">{{i}}</option>
              % end
            % end
          </select>
          <label>Širina:</label>
    
        </div>
        <script>
          $(document).ready(function() {
            $('select').material_select();
          });
          </script>

      <div class="input-field col s6">
        <select name= "visina">
          % for i in range(3, 6):
            % if i == 5:
              <option value="{{i}}" selected>{{i}}</option>
            % else:
              <option value="{{i}}">{{i}}</option>
            % end
          % end
        </select>
        <label>Višina:</label>
        </div>
        <script>
          $(document).ready(function() {
            $('select').material_select();
          });
        </script>
    </div>

<!--text
      <div class="row">
        <div class="input-field col s6">
          <input placeholder="Placeholder" id="first_name" type="text" class="validate">
          <label>First Name</label>
        </div>
        <div class="input-field col s6">
          <input id="last_name" type="text" class="validate">
          <label for="last_name">Last Name</label>
        </div>
      </div>-->

      <button class="{{tip}}" type="submit">
        Ustvari svoj nivo
        <!-- <i class="material-icons right">send</i>  za ikonco -->
      </button>
    </form>
  