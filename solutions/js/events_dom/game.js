var l = new Labyrinth();

function keyhandle(event) {
    switch (event.keyCode) {
        case 37: // left
            l.move(-1, 0);
            break;
        case 38: // up
            l.move(0, -1);
            break;
        case 39: // right
            l.move(1, 0);
            break;
        case 40: // down
            l.move(0, 1);
            break;
        default: // any other key
            // do nothing
            break;
    }
}

window.onload = function() {
    //l.printConsole();
    l.printDisplay("map");

    document.body.addEventListener("keyup", keyhandle);
}
