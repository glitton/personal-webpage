"use strict"

$(document).ready(function(){
    // Stops YouTube video when modal window is closed

    // PAWS video
    $('#close-paws').on('click', function(){
        var video = $('#paws').attr('src');
          $('#paws').attr('src','');
          $('#paws').attr('src', video);
        }
      )

    // Hitachi Oracle video
    $('#close-oracle').on('click', function(){
        var video = $('#oracle').attr('src');
          $('#oracle').attr('src','');
          $('#oracle').attr('src', video);
        }
      )





});
