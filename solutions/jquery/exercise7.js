$(document).ready(function () {
    $("input[type='password']").keyup(function () {

        var pw1 = $("#password1").val();
        var pw2 = $("#password2").val();

        var isError = false;
        if (pw1.length > 0) {
            if (pw1.length < 6) {
                $("#pw1_check").html("Too short");
                isError = true;
            }
            else {
                $("#pw1_check").html("");
            }
            if (pw2.length > 0 && pw1 !== pw2) {
                $("#pw2_check").html("The two passwords don't match");
                isError = true;
            }
            else {
                $("#pw2_check").html("");
            }
        }
        else {
            $("#pw1_check").html("");
        }

        // show the submit button only if everything is ok
        if (pw1.length > 0 && pw2.length > 0 && !isError) {
            $("#submitBtn").show();
        }
        else {
            $("#submitBtn").hide();
        }
    });
});

