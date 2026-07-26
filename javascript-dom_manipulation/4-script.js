const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const item = document.createElement('li');
  item.textContent = 'Item';
  myList.appendChild(item);
});
