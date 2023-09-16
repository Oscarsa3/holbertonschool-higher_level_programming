const api = "https://swapi-api.hbtn.io/api/films/?format=json";
const ul = document.getElementById("list_movies");
fetch(api)
.then(response => response.json())
.then(data => {
    const movies = data.results;
    movies.forEach(movie => {
        const newLi = document.createElement("li");
        newLi.textContent = movie.title
        ul.appendChild(newLi);
    });
});