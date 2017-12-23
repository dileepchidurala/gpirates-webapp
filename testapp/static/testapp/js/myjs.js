$("#requestButton").on("click", function(){

  var  name = $("#name").val();
  var description = $("#download").val();
  $("#download").val("");
  $("#name").val("");
  console.log(name + " " + description);
  $.ajax({
    url: base + '/app/addrequest/',
    dataType: "json",
    type: "POST",
    data: {
      'name': name,
      'requestDetail': description,
    },
    crossDomain: true,
    success: function(result) {
      $("#modalcontent").hide();
      $("#success").show();
      $("#success").html('<svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/></svg>');
      $("#success").append("<center>Your Download will be processed within 12 hours<br>Keep checking for new uploads :)</center><br><br>");
      // $("#modalFooter").css("textAlign", "center");
    },
    error: function(resp, ajaxoption, thrownerror) {
        console.log("error");
    }
  });
})

$("#requestModal").on("click", function(){
  $("#modalcontent").show();
  $("#success").hide();
});

$("#reportButton").on("click", function(){
    var  name = "problem user"
    var description = "PROBLEM: " + $("#problem").val();
    $("#problem").val("");
    $.ajax({
      url: base + '/app/addrequest/',
      dataType: "json",
      type: "POST",
      data: {
        'name': name,
        'requestDetail': description,
      },
      crossDomain: true,
      success: function(result) {
        $("#modalcontent1").hide();
        $("#success1").show();
        $("#success1").html('<svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/></svg>');
        $("#success1").append("<center>Your Problem has been reported. It will be handled.<br>Keep checking for new uploads :)</center><br><br>");
        // $("#modalFooter").css("textAlign", "center");
      },
      error: function(resp, ajaxoption, thrownerror) {
          console.log("error");
      }
    });
  })
  
  $("#reportModal").on("click", function(){
    $("#modalcontent1").show();
    $("#success1").hide();
  });
  
  