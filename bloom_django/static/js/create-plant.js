/**
 * Created by Miranda on 9/5/15.
 */

$(document).ready(function () {

    var plantType;
    var plantName;
    var bg;

    $(".plant-pick").on("submit", function (event) {
        event.preventDefault();
        $(".title").remove();
        $(".plant-pick").addClass("plant-name");
        $(".plant-name").removeClass("plant-pick");
        $(".subtitle").replaceWith("<p class=\"subtitle\"> Give it a name: </p>");
        $(".plant-pick-container").replaceWith("<input class=\"plant-name-box\" type=\"text\" name=\"plant-name-box\"><br /><input class=\"go\" type=\"submit\" value=\"Go!\" style=\"font-size:15px;padding:5px;\">");

        $(".plant-name").on("submit", function (event) {
            event.preventDefault();
            plantName = $(".plant-name-box").val();
            $(".plant-name").addClass("bg-pick");
            $(".bg-pick").removeClass("plant-name");
            $(".go").remove();
            $(".subtitle").replaceWith("<p class=\"subtitle\"> Choose a background: </p>");
            $(".plant-name-box").replaceWith("<div class=\"bg-pick-container\"><input type=\"image\" src=\"http://placehold.it/250x250\" alt=\"Background 1\"><input type=\"image\" src=\"http://placehold.it/250x250\" alt=\"Background 2\"><input type=\"image\" src=\"http://placehold.it/250x250\" alt=\"Background 3\"> </div>");

            $(".bg-pick").on("submit", function (event) {
                $(".bg-pick-container").remove();
                $(".subtitle").replaceWith("<p style=\"color:#ff009c;\">You're all set! Ready to play? </p><a href=\"play.html\" style=\"font-size:25px;text-decoration:none;color:#90b63f;\">Take me to the game! -></p>");

                $.ajax({
                    url: '/create.html',
                    dataType: 'text',
                    type: 'post',
                    data: $(this).serialize(),
                    success: function (plantType, plantName, bg) {
                       }
                });

            });
        });
    });


});



