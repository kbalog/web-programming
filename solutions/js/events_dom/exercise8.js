function initGrid() {
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

    // creating colored tiles
    var cdiv = document.getElementById("colors");
    for (var i = 0; i < colors.length; i++) {
        var tile = document.createElement("div");
        tile.className = "choice";
        tile.style.backgroundColor = colors[i];
        tile.addEventListener("click", tileClicked);
        cdiv.appendChild(tile);
    }
}

function tileClicked() {
    var color = this.style.backgroundColor;
    var sel = document.getElementById("selected");
    sel.style.backgroundColor = color;
    sel.innerHTML = color;
}

window.onload = function () {
    initGrid();
}
