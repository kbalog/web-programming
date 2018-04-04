function getResponse() {
    var xhr = new XMLHttpRequest();
    
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            document.getElementById("status").innerHTML = "MD5: " + result;
            /* show button */
            document.getElementById("submit").style.display = "block";
        }
    };
    var pw = document.getElementById("pw").value;
    var vars = "pw=" + pw;

    /* sending the request using POST */
    xhr.open("POST", "/get_pw", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(vars);

    /* display loading bar */
    document.getElementById("status").innerHTML = "<img src='/static/loading.gif' />";
    /* hide button */
    document.getElementById("submit").style.display = "none";
}
