var CELL_SIZE = 40;
var START_ROW = 0, START_COL = 0;
var END_ROW = 3, END_COL = 5;
var CHARACTER_ID = "character";

function Labyrinth() {
    this.map = [
        [0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0]];
    this.pos_x = START_COL;
    this.pos_y = START_ROW;
}


function printConsole() {
    for (var y = 0; y < this.map.length; y++) {
        var line = "";
        for (var x = 0; x < this.map[y].length; x++) {
            line += (this.map[y][x] == 1) ? "*" : " ";
        }
        console.log(line);
    }
}

// utility function to set the position of a given element on the map
function setMapPosition(element, x, y) {
    element.style.left = x * CELL_SIZE + "px";
    element.style.top = y * CELL_SIZE + "px";
}


function addCell(parent, pos_x, pos_y, bgcolor) {
    var cell = document.createElement("div");
    cell.style.width = CELL_SIZE + "px";
    cell.style.height = CELL_SIZE + "px";
    cell.style.backgroundColor = bgcolor;
    cell.style.position = "absolute";
    setMapPosition(cell, pos_x, pos_y);
    parent.appendChild(cell);
}

function addCharacter(parent) {
    var c = document.createElement("img");
    c.src = "images/hero.jpg";
    c.id = CHARACTER_ID;
    c.style.width = CELL_SIZE + "px";
    c.style.height = CELL_SIZE + "px";
    c.style.position = "absolute";
    setMapPosition(c, this.pos_x, this.pos_y);
    parent.appendChild(c);
}

function printDisplay(id) {
    // print map area with border
    var parent = document.getElementById(id);
    parent.style.position = "absolute";
    parent.style.overflow = "auto";
    parent.style.border = "1px solid black";
    parent.style.width = this.map[0].length * CELL_SIZE + "px";
    parent.style.height = this.map.length * CELL_SIZE + "px";

    // print cells
    for (var y = 0; y < this.map.length; y++) {
        for (var x = 0; x < this.map[y].length; x++) {
            addCell(parent, x, y, (this.map[y][x] == 1) ? "grey" : "white");
        }
    }

    // print destination cell
    addCell(parent, END_COL, END_ROW, "yellow");

    // print character at starting position
    addCharacter(parent);
}

function move(x, y) {
    var new_x = this.pos_x + x;
    var new_y = this.pos_y + y;

    // check if we stay within the map
    if (new_x < 0 || new_x >= this.map[0].length
        || new_y < 0 || new_y >= this.map.length)
        return;

    // check if we would step on a free cell
    if (this.map[new_y][new_x] == 0) {
        this.pos_x = new_x;
        this.pos_y = new_y;
        var c = document.getElementById(CHARACTER_ID);
        setMapPosition(c, new_x, new_y);

        // check if we reached the destination
        if (this.pos_x == END_COL && this.pos_y == END_ROW) {
            alert("Congratulations!");
        }
    }
}

Labyrinth.prototype.printConsole = printConsole;
Labyrinth.prototype.printDisplay = printDisplay;
Labyrinth.prototype.move = move;
