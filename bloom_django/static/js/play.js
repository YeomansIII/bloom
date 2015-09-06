/**
 * Created by minh on 9/5/15.
 */

$(document).ready(function() {
  $('#game-menu-mobile').slicknav();
  $('.watering-can').click(function() {
    $.ajax({
      url: '/play/',
      dataType: 'text',
      type: 'post',
      success: function(data, status) {
        if (data === 'error') {
          alert("An error has occurred!");
        } else {
          /* Take new image and make that replace the old one plus some pretty animation. */
          $('.flower').replaceWith('<div class="flower animate fadeIn"> <img src="' + data + '" </div>');
        }
      }
    });
  });

});


window.onload = function() {
  var background = $(".flower").children()[0].src;
  var dayIndex = background.indexOf("Day");
  var pngIndex = background.indexOf(".png");
  var picNo = Number(background.substring(dayIndex + 3, pngIndex));
  var dates = $(".sliver-date");
  for (var i = 0; i < picNo; i++) {
    dates[9 - i].style.color = "#fff";
  }
}
