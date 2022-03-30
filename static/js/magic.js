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
      var txtval = parts[1].trim();
      console.log(textval + " " + name);
      var s = txtval.substring(1, 3);
      var d = txtval.substring(4, 5);
      var a = txtval.substring(6, 8);

      $("#fS").val(s);
      $("#fS").val(s);
      $("#fD").val(d);
      $("#fA").val(a);

      $("#btnUpdate").click(function(e){

          var ss = $("#fS").val();
          var dd = $("#fD").val();
          var aa = $("#fA").val();
          var ff = $("#fF").val();

          var error = 3;
          if(ss >= 1 && ss <= 998){
            console.log("speed: " + ss);
            error--;
          }

          if(dd >= 0 && dd <= 1 ){
            console.log("dir: " + dd);
            error--;
          }

          if(aa >= 0 && aa <= 1080){
            console.log("angle: " + aa);
            error--;
          }

          if(error == 0){
            console.log("all good");
            var aal = aa.length;
            console.log("ll: " + aal);
            if(aal == 1){ aa = "00" + aa; }
            if(aal == 2){ aa = "0" + aa; }
            var steps = "D"+ss+dd+aa;
            console.log("steps: " + steps);
            console.log()
            window.location.href = '/updatefile/' + ff + '/' + steps;

          } else {

            $("#errorMsg").html("Please, check your values! Something is not right");
          }

      });

    }



});



function sendFileUpdate(){

}
