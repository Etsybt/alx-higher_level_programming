$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // 13 is the ASCII code for the Enter key
      fetchTranslation();
    }
  });
});
