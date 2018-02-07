/**
 * Exercise #9: Countdown timer
 */

var timeLeft = -1;  // global variable, stores time left (in seconds)

$(document).ready(function () {

    $("form[name='countdown_form']").submit(function(e) {

        e.preventDefault();  // preventing the form from submission

        // set time left (seconds)
        timeLeft = $("#minutes").val() * 60;

        $(this).hide();  // hide form
        $("#countdown").show();  // show countdown div

    });

});