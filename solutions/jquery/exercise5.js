/**
 * Exercise #5: jQuery color picker
 */

$(document).ready(function () {

    // collect colors in an array
    var colors = [];
    var range = ["00", "33", "66", "99", "cc", "ff"];

    for (var r = 0; r < range.length; r++) {
        for (var g = 0; g < range.length; g++) {
            for (var b = 0; b < range.length; b++) {
                colors.push("#" + range[r] + range[g] + range[b]);
            }
        }
    }

    // create colored tiles
    for (var i = 0; i < colors.length; i++) {
        var tile = $("<div></div>");
        tile.addClass("choice");
        tile.css("background-color", colors[i]);
        // we store the hex color value in a separate attribute as well
        // (the background-color css property could also be used, but that returns
        // colors in rbg(R,G,B) format instead of #RRGGBB)
        tile.attr("hexcode", colors[i]);
        $("#colors").append(tile);
    }

    // when a tile is clicked
    $(".choice").click(function () {
        var color = $(this).attr("hexcode");
        $("#selected").html(color);
        $("#selected").css("background-color", color);
    });

});
