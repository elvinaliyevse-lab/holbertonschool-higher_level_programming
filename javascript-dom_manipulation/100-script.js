window.addEventListener('DOMContentLoaded', function () {
  const myList = document.querySelector('.my_list');

  document.querySelector('#add_item').addEventListener('click', function () {
    const item = document.createElement('li');
    item.textContent = 'Item';
    myList.appendChild(item);
  });

  document.querySelector('#remove_item').addEventListener('click', function () {
    const last = myList.lastElementChild;
    if (last) {
      myList.removeChild(last);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function () {
    while (myList.firstElementChild) {
      myList.removeChild(myList.firstElementChild);
    }
  });
});
