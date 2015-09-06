/**
 * Created by minh on 9/5/15.
 */
window.onload = function() {
    var background = $(".flower").children()[0].src;
    var dayIndex = background.indexOf("Day");
    var pngIndex = background.indexOf(".png");
    var picNo = Number(background.substring(dayIndex + 3, pngIndex));
    var dates = $(".sliver-date");
    for (var i = 0; i <= picNo; i++) {
        dates[9 - i].removeAttribute("hidden");
    }
}
