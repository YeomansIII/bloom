/**
 * Created by minh on 9/5/15.
 */

$( document ).ready( function() {
        $('#game-menu-mobile').slicknav();
    $('.watering-can').on('click', function(){
        var background = $(".flower").children()[0].src;
        var dayIndex = background.lastIndexOf("Day");
        var pngIndex = background.lastIndexOf(".png");
        var picNo = Number(background.substring(dayIndex + 3, pngIndex));
        if (picNo == 2) {
            alert("3 Consecutive Days! Unlocked a new flower pot.");
        }

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
