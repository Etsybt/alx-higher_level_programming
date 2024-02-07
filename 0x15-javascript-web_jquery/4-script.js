const $toggleHeader = $('#toggle_header');
const $headerElem = $('header');

$toggleHeader.click(function () {
  if ($headerElem.hasClass('red')) {
    $headerElem.removeClass('red').addClass('green');
  } else {
    $headerElem.removeClass('green').addClass('red');
  }
});
