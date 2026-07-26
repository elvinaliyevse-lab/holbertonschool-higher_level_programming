const header = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', function () {
  if (header.className === 'red') {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
});
