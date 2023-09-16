const api = "https://swapi-api.hbtn.io/api/people/5/?format=json";
fetch(api)
.then(response => response.json())
.then(name => document.getElementById("character").textContent = name.name);