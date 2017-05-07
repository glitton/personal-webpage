"use strict"

$(document).ready(function(){
    // Stops YouTube video when modal window is closed
    $("#portfolioModal1").on('hidden.bs.modal', function (evt) {
      $("#pawsvideo").attr("src", $("#pawsvideo").attr("src"));
    });




});
