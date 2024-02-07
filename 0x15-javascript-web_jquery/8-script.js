$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const films = data.results;
  const $listMovies = $('#list_movies');

  films.forEach(function (film) {
    $listMovies.append(`<li>${film.title}</li>`);
  });
});
