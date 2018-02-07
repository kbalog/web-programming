/**
 * Exercise #8: Card board
 */

$(document).ready(function() {

    /* dealing cards */
    $("form[name='layout_form']").submit(function(e) {

        e.preventDefault();  // preventing the form from submission

        $("#cardboard").empty();

        var layout = $("#layout").val();
        var dim = layout.split("x");
        var sizeCols = dim[0];
        var sizeRows = dim[1];

        var card;
        for (var row = 0; row < sizeRows; row++) {
            for (var col = 0; col < sizeCols; col++) {
                card = $("<div></div>").addClass("card");
                if (col == 0) {
                    card.addClass("clearleft");
                }
                $("#cardboard").append(card);
            }
        }

        var cardWidth = card.outerWidth(true);
        $("#cardboard").width(sizeCols * cardWidth);

        // alternatively, we can return false to prevent the form from submitting
        //return false;
    });

    /* clicking on a card */
    $("#cardboard").on("click", ".card", function () {
        $(this).fadeTo(1000, 0);
    });

});