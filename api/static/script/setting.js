/* global $ */

let degree = document.getElementById("degree");
let speed = document.getElementById("speed");

let cel = document.querySelectorAll("#C°");
let fah = document.querySelectorAll("#F°");

let kph = document.getElementById("kph");
let mph = document.getElementById("mph");

fah.forEach((f) => {
  f.setAttribute("id", "nondispaly")
})
mph.setAttribute("id", "nondispaly")


degree.addEventListener("change", () => {
  // Get the selected option value
  if (degree.value === "#C°") {
    fah.forEach((f) => {
      f.setAttribute("id", "nondispaly")
    })
    cel.forEach((c) => {
      c.setAttribute("id", "C°")
    })
  } else {
    cel.forEach((c) => {
      c.setAttribute("id", "nondispaly")
    })
    fah.forEach((f) => {
      f.setAttribute("id", "F°")
    })
  }
});

speed.addEventListener("change", () => {

  if (speed.value === "#kph") {
    mph.setAttribute("id", "nondispaly")
    kph.setAttribute("id", "kph")
  } else {
    kph.setAttribute("id", "nondispaly")
    mph.setAttribute("id", "mph")
  }
});
