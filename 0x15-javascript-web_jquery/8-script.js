$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const titles = data.results;
    for (let i = 0; i < titles.length; i++) {
      const title = $('<li></li>').text(titles[i].title);
      $('UL#list_movies').append(title);
    }
  });
});
