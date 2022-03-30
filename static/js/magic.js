$( document ).ready(function() {
    console.log( "Welcome to the machine!" );

    $('body').on('click', '.gB', function(e){
      e.preventDefault();
      var gotoVal = $(this).attr('href');
      $.get( "/arduino/" + gotoVal );
    });



    if($('body').hasClass( "edit" )){

      var txtval = $("#txtval").val();
      var parts = txtval.split(':');
      var name = parts[0].trim();
      txtval = parts[1].trim();
      var m = txtval.substring(0, 1);
      var a = 0;
      var d = 0;
      var s = 0;


      if(m == "L"){
        hideFields(m);

        a = txtval.substring(1, 4);

        // Fields Population
        $("#fN").val(name);
        $("#fM").val(m);
        $("#fDP").val(a);

      }

      if(m == "D"){
        hideFields(m);

        s = txtval.substring(1, 4);
        d = txtval.substring(4, 5);
        a = txtval.substring(5, 9);

        $("#fN").val(name);
        $("#fM").val(m);
        $("#fS").val(s);
        $("#fD").val(d);
        $("#fA").val(a);
      }

      function hideFields(mode){
        if(mode == "L"){
          $(".modeD").hide();
          $(".modeL").show();
        }else{
          $(".modeL").hide();
          $(".modeD").show();
        }
      }

      $("#fM").change(function(){
        if($("#fM").val() == "L"){
          hideFields("L");
        }else{
          hideFields("D");
        }
      });



      $("#btnUpdate").click(function(e){

          var nn = $("#fN").val();
          var mm = $("#fM").val();
          var ss = $("#fS").val();
          var dd = $("#fD").val();
          var aa = $("#fA").val();
          var fdp = $("#fDP").val();
          var ff = $("#fF").val();



          if(mm == "L"){
            var fdpl = fdp.length;
            if(fdpl == 1){ fdp = "00" + fdp; }
            if(fdpl == 2){ fdp = "0" + fdp; }
            var sendMsg = nn+":L"+fdp;
            window.location.href = '/updatefile/' + ff + '/' + sendMsg;
          }

          if(mm == "D"){

            //SPEED ###
            var ssl = ss.length;
            if(ssl == 1){ ss = "00" + ss; }
            if(ssl == 2){ ss = "0" + ss; }

            // DEGREEs ####
            var aal = aa.length;
            if(aal == 1){ aa = "000" + aa; }
            if(aal == 2){ aa = "00" + aa; }
            if(aal == 3){ aa = "0" + aa; }

            var sendMsg = nn+":D"+ss+d+aa;
            window.location.href = '/updatefile/' + ff + '/' + sendMsg;
          }



      });

    }



});



function sendFileUpdate(){

}
