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

        // TODO set class="choice" for the tile and set background color to colors[i]
        // Hint: you can use the css() method to set the background color

        // TODO append tile to the element with id="colors"
    }

    // when a tile is clicked
    $(".choice").click(function () {
        // TODO: get the color of the tile and write it to the element id="selected"
    });

});
