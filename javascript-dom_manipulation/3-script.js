const header = document.querySelector("header");
const change = document.getElementById("toggle_header");
change.addEventListener("click", function () {
    if (header.className === "green") {
        header.className = "red";
    } else {
        header.className = "green";
    }
});