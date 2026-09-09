document.write("<br>")
document.write("From the script file.")

var input = "frog";
document.write(input);

for (var i = 0; i < 5; i++) {
  document.write(i);
  document.write("<br>")
}

var obj = {};
obj.name = "Simon";
var name = obj.name;

document.write(name);
document.write(obj["name"]);

var obj2 = {
	name: "Default",
	age: 12,
	
	size: {
		height: 6.2,
		weight: 200
	}
}

obj2.name  = "george";
obj2.age = 18;

document.write(obj2.name);
document.write(obj2.age);
document.write(obj2.size.height);

function add(a, b) {
	var total = a + b;
	return total;
}

document.write("Add's results:")
document.write("<br>");
document.write(add(3, 4));


function funcRunner(fn, x, y){
	return fn(x, y);
}

document.write("<br>");
document.write("funcRunner's results:")
document.write("<br>");
document.write(funcRunner(add, 3, 5));