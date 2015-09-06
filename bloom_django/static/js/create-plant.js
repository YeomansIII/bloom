/**
 * Created by Miranda on 9/5/15.
 */

$(document).ready(function() {

  var plantType;
  var plantName;
  var bg;
  var $plantpick = $('.plant-pick');
  var $namepick = $('.name-pick');
  var $bgpick = $('.bg-pick');

  window.setTimeout(function() {
    $('.loading-icon').hide();
    $plantpick.fadeIn('slow');
  }, 1500);
  $("#plant-pick").imagepicker();
  $("#bg-pick").imagepicker();

  $(".plant-pick-next").click(function() {
    $('.title').remove();
    plantType = $("#plant-pick").val();
    if (plantType === '') {
      alert("Please select a plant type!");
    } else {
      $plantpick.slideUp('fast');
      $namepick.slideDown('fast');
    }
  });

  $('.name-pick-next').click(function() {
    plantName = $('.plant-name-box').val();
    if (plantName === '') {
      alert("Please type a plant name!");
    } else {
      $namepick.slideUp('fast');
      $bgpick.slideDown('fast');
    }
  });

  $('.bg-pick-next').click(function() {
    bg = $("#bg-pick").val();
    if (bg === '') {
      alert("Please select a background!");
    } else {
      var postdata = {
        plantType: plantType,
        plantName: plantName,
        background: bg
      }
      $.ajax({
        url: '/create/',
        dataType: 'text',
        type: 'post',
        data: postdata,
        success: function(data, status) {
          if (data === 'error') {
            alert("An error has occurred!");
          } else {
            $bgpick.slideUp('fast');
            var $ready = $('.ready-to-play');
            $ready.fadeIn('fast');
            $ready.find('a').attr('href', data);
          }
        }
      });
    }
  });
});
