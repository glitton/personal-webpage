"use strict"

$(document).ready(function(){
    // Stops YouTube video when modal window is closed
    $('.close-youtube').on('click', function(){
        var video = $('.you-tube').attr('src');
          $('.you-tube').attr('src','');
          $('.you-tube').attr('src', video);
        }
      )
  });
