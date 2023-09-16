document.addEventListener("DOMContentLoaded", function () {
    const api = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    fetch(api)
    .then(response => response.json())
    .then(say => document.getElementById("hello").textContent = say.hello);
});