/* Dog class - to be used in objects.html */

function Dog(name, weight, breed) {
    this.name = name;
    this.weight = weight;
    this.breed = breed;
}

function printInfo() {
    console.log("name:   " + this.name);
    console.log("weight: " + this.weight);
    console.log("breed:  " + this.breed);
}

// Adding an info() method to the Dog prototype
Dog.prototype.info = printInfo;

var mydog = new Dog("Tiffy", 3.4, "mixed");
mydog.info();

if (mydog instanceof Dog) {
    console.log("it's a dog");
}
