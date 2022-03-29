
/*function test(){

  var obj;

  fetch('static/1.txt')
    .then(response => response.text())
    .then(data => obj = data);
    // outputs the content of the text file
    console.log(obj);
}

*/



$( document ).ready(function() {
    console.log( "ready!" );
    /*
    $(".gB").click(function(e){
      e.preventDefault();
      var gotoVal = $(this).attr('href');
      $.get( "/move/" + gotoVal );
    });


    $(".gB").live('click', function(e){
      e.preventDefault();
      var gotoVal = $(this).attr('href');
      $.get( "/move/" + gotoVal );
    });
    */

    $('body').on('click', '.gB', function(e){
      e.preventDefault();
      var gotoVal = $(this).attr('href');
      $.get( "/arduino/" + gotoVal );
    });



    if($('body').hasClass( "edit" )){

      var txtval = $("#txtval").val();
      var s = txtval.substring(1, 2);
      var d = txtval.substring(3, 4);
      var a = txtval.substring(5, 8);

      $("#fS").val(s);
      $("#fD").val(d);
      $("#fA").val(a);

      console.log(a);
      //('00' + s).slice(-3)  // '004'

      $("#btnUpdate").click(function(e){

          var ss = $("#fS").val();
          var dd = $("#fD").val();
          var aa = $("#fA").val();
          var ff = $("#fF").val();

          var error = 3;
          if(ss >= 1 && ss <= 9){
            console.log("speed: " + ss);
            error--;
          }

          if(dd >= 1 && dd <= 9){
            console.log("dir: " + dd);
            error--;
          }

          if(aa >= 0 && aa <= 360){
            console.log("angle: " + aa);
            error--;
          }

          if(error == 0){
            console.log("all good");
            var aal = aa.length;
            console.log("ll: " + aal);
            if(aal == 1){ aa = "00" + aa; }
            if(aal == 2){ aa = "0" + aa; }
            var steps = ss+dd+aa;
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
