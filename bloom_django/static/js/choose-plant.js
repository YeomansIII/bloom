/**
 * Created by Miranda on 9/5/15.
 */
var $plantpick = $('.plant-pick');

window.setTimeout(function() {
  $('.loading-icon').hide();
  $plantpick.fadeIn('slow');
}, 1500);
$("#plant-pick").imagepicker();
