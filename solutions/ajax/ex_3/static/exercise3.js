/**
 * This file is part of Exercise #3
 */

$(document).ready(function () {
    $("#username").blur(function () {
        var url = "/check_username?username=" + $(this).val();
        $("#username_status").load(url);
    });
});
