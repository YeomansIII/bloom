/**
 * Created by minh on 9/5/15.
 */

$( document ).ready( function() {
        $('#game-menu-mobile').slicknav();
    $('.watering-can').on('click', function(){
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
