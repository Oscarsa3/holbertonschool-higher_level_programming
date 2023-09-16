const update = document.getElementById("update_header");
update.addEventListener("click", function () {
    const header = document.querySelector("header");
    header.textContent = "New Header!!!";
});