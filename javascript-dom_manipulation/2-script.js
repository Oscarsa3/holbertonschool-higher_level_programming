const header = document.querySelector("header");
const change = document.getElementById("red_header");
change.addEventListener("click", function () {
    header.className = "red";
});