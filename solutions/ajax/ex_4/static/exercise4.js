/**
 * This file is part of Exercise #4
 */

$(document).ready(function () {
    $("#item_id").blur(function () {
        var item_id = $(this).val();
        if (item_id.length == 3) { /* if item id is 3 digits */
            $.get("/inventory", {"item_id": item_id}, function (data) {
                var result = JSON.parse(data);
                /* fill in form fields */
                $("#name").val(result.name);
                $("#brand").val(result.brand);
                $("#size_x").val(result.size_x);
                $("#size_y").val(result.size_y);
                $("#size_z").val(result.size_z);
                $("#price").val(result.price);
                $("#available").prop("checked", result.available);
            });
        }
        else {
            /* clear form values */
            $("#name").val("");
            $("#brand").val("");
            $("#size_x").val("");
            $("#size_y").val("");
            $("#size_z").val("");
            $("#price").val("");
            $("#available").prop("checked", false);
        }
    });
});

