/**
 * Created by Miranda on 9/5/15.
 */

$(document).ready(function () {

    $(".plant-pick").on("submit", function (event) {
        event.preventDefault();
        $(".plant-pick").addClass("plant-name");
        $(".plant-name").removeClass("plant-pick");
        $(".subtitle").replaceWith("<p class=\"subtitle\"> Give it a name: </p>");
        $(".plant-pick-container").replaceWith("<input class=\"plant-name-box\" type=\"text\" name=\"plant-name-box\"><input class=\"go\" type=\"submit\" value=\"Go!\" style=\"font-size:15px;padding:5px;\">");


        $(".plant-name").on("submit", function(event){
            console.log("TEST");
            event.preventDefault();
            $(".plant-name").addClass("bg-pick");
            $(".bg-pick").removeClass("plant-name");
            $(".subtitle").replaceWith("<p class=\"subtitle\"> Choose a background: </p>");
            $(".plant-name-box").replaceWith("<div class=\"bg-pick-container\"><input type=\"image\" src=\"http://placehold.it/250x250\" alt=\"Background 1\"><input type=\"image\" src=\"http://placehold.it/250x250\" alt=\"Background 2\"><input type=\"image\" src=\"http://placehold.it/250x250\" alt=\"Background 3\"> </div>");

        $(".bg-pick").on("submit", function(event){
           $(".subtitle").replaceWith("<h2>You're all set! Ready to play? </h2>");
            $(".bg-pick-container").remove();
            $(".go").remove();
        });

        });


    });



});



