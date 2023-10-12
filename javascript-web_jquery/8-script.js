fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    data.results.forEach(movie => {
        $('#list_movies').append(`<li>${movie.title}</li>`)
    })
})