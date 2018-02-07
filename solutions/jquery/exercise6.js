$(document).ready(function () {
    $("#addButton").click(function () {
        var songName = $("#songTextInput").val();
        if (songName == "") {
            alert("Please enter a song");
        }
        else {
            // create <li> element with jQuery
            var li = $("<li></li>").html(songName);
            // append element to list
            $("#playlist").append(li);
        }
    });
});
