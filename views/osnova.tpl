<!DOCTYPE html>
<html>

<head>
  <style>
    .osnovni:hover {
      background: rgba(0, 0, 0, .3);
    }

    .poudarjen {
      background: rgba(0, 0, 0, .2);
    }

    .poudarjen:hover {
      background: rgba(0, 0, 0, .5);
    }

    .spodnji {
      position: relative;
      top: 0;
      left: 0;
    }

    .nespodnji {
      position: absolute;
      top: 0;
      left: 50%;
      /* to je zato, ker zdaj uporabljamo text-align: center. Brez tega je nespodnja slika preveč levo */
      transform: translate(-50%, 0);
    }

    form + form {
      margin-top: 10px;
    }

    table + form {
      margin-top: 10px;
    }

    .divider,
    button {
      margin-bottom: 10px;
      margin-top: 10px;
    }

    .row .input-field input:focus {
      border-bottom: 1px solid darkgreen;
      box-shadow: 0 1px 0 0 darkgreen;
    }
  </style>

  <!--Import Google Icon Font-->
  <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

  <!--Import materialize.css-->
  <!-- Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">

  <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>

  <!-- Compiled and minified JavaScript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>

  <!--Let browser know website is optimized for mobile-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

</head>

<body onLoad="window.scroll(0, 155)">
  <div class="card-panel teal lighten-2">
    <h3 style="color: white;">
      Skladiščnik
    </h3>
  </div>
  <div class="divider"></div>

  <div class="container">
    {{!base}}
    <div class="divider"></div>
  </div>

</body>

</html>