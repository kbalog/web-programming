function checkLicense() {
    var name = document.getElementById("name").value;
    var license = document.getElementById("license").value;
    /* send the request if both name and license are filled in */
    if (name.length > 0 && license.length > 0) {
        var xhr = new XMLHttpRequest();
        /* register an embedded function as the handler */
        xhr.onreadystatechange = function () {
            /* readyState = 4 means that the response has been completed
             * status = 200 indicates that the request was successfully completed */
            if (xhr.readyState == 4 && xhr.status == 200) {
                var result = xhr.responseText;
                document.getElementById("license_check").innerHTML = result;
            }
        };
        /* send the request using POST */
        xhr.open("POST", "/check_license", true);
        /* To POST data like an HTML form, add an HTTP header */
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        /* variables go in the request body */
        xhr.send("name=" + name + "&license=" + license);
    }
    else {
        /* clear status area if name or license are empty */
        document.getElementById("license_check").innerHTML = "";
    }
}
