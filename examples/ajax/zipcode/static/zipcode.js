/* get place from postcode */
function getPlace(postcode) {
    var xhr = new XMLHttpRequest();
    /* register an embedded function as the handler */
    xhr.onreadystatechange = function () {
        /* readyState = 4 means that the response has been completed
         * status = 200 indicates that the request was successfully completed */
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            document.getElementById("place").value = result;
        }
    };
    /* send the request using GET */
    xhr.open("GET", "/getplace?postcode=" + postcode, true);
    xhr.send(null);
}
