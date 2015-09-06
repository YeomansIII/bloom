/**
 * Created by Miranda on 9/5/15.
 */
/**
 * Created by Miranda on 9/5/15.
 */

$(document).ready(function () {

    var plantType;
    var plantName;
    var bg;
    var $plantpick = $('.plant-pick');
    var $namepick = $('.name-pick');
    var $bgpick = $('.bg-pick');

    $("#plant-pick").imagepicker();
    $("#bg-pick").imagepicker();

    plantType = $("#plant-pick").val();
    plantName = $('.plant-name-box').val();
    bg = $("#bg-pick").val();

    $(".save").on("submit", function () {
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
            success: function (data, status) {
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
    });

});