// ****** select items **********

const form = document.querySelector(".to-do-list");
const alert = document.querySelector(".alert");
const taskToDo = document.getElementById("task-to-do");
const submitButton = document.querySelector(".submit-button");
const container = document.querySelector(".tasks-container");
const list = document.querySelector(".tasks-list");
const clearButton = document.querySelector(".clear-button");
// edit option
let editElement;
let editFlag = false;
let editID = "";
// ****** event listeners **********

// submit form
form.addEventListener("submit", addItem);
// clear list
clearButton.addEventListener("click", clearItems);
// display items onload
window.addEventListener("DOMContentLoaded", setupItems);

// ****** functions **********

// add item
function addItem(e) {
  e.preventDefault();
  const value = taskToDo.value;
  const id = new Date().getTime().toString();

  if (value !== "" && !editFlag) {
    createListItem(id, value);
    // display alert
    displayAlert("item added to the list", "success");
    // show container
    container.classList.add("show-container");
    // set local storage
    addToLocalStorage(id, value);
    // set back to default
    setBackToDefault();
  } else if (value !== "" && editFlag) {
    editElement.innerHTML = value;
    displayAlert("value changed", "success");

    // edit  local storage
    editLocalStorage(editID, value);
    setBackToDefault();
  } else {
    displayAlert("please enter value", "danger");
  }
}
// display alert
function displayAlert(text, action) {
  alert.textContent = text;
  alert.classList.add(`alert-${action}`);
  // remove alert
  setTimeout(function () {
    alert.textContent = "";
    alert.classList.remove(`alert-${action}`);
  }, 1000);
}

// clear items
function clearItems() {
  const items = document.querySelectorAll(".task-item");
  if (items.length > 0) {
    items.forEach(function (item) {
      list.removeChild(item);
    });
  }
  container.classList.remove("show-container");
  displayAlert("empty list", "danger");
  setBackToDefault();
  localStorage.removeItem("list");
}

// delete item

function deleteItem(e) {
  const element = e.currentTarget.parentElement.parentElement;
  const id = element.dataset.id;

  list.removeChild(element);

  if (list.children.length === 0) {
    container.classList.remove("show-container");
  }
  displayAlert("item removed", "danger");

  setBackToDefault();
  // remove from local storage
  removeFromLocalStorage(id);
}
// edit item
function editItem(e) {
  const element = e.currentTarget.parentElement.parentElement;
  // set edit item
  editElement = e.currentTarget.parentElement.previousElementSibling;
  // set form value
  taskToDo.value = editElement.innerHTML;
  editFlag = true;
  editID = element.dataset.id;
  //
  submitButton.textContent = "edit";
}
// set backt to defaults
function setBackToDefault() {
  taskToDo.value = "";
  editFlag = false;
  editID = "";
  submitButton.textContent = "submit";
}

// ****** local storage **********

// add to local storage
function addToLocalStorage(id, value) {
  const taskToDo = { id, value };
  let items = getLocalStorage();
  items.push(taskToDo);
  localStorage.setItem("list", JSON.stringify(items));
}

function getLocalStorage() {
  return localStorage.getItem("list")
    ? JSON.parse(localStorage.getItem("list"))
    : [];
}

function removeFromLocalStorage(id) {
  let items = getLocalStorage();

  items = items.filter(function (item) {
    if (item.id !== id) {
      return item;
    }
  });

  localStorage.setItem("list", JSON.stringify(items));
}
function editLocalStorage(id, value) {
  let items = getLocalStorage();

  items = items.map(function (item) {
    if (item.id === id) {
      item.value = value;
    }
    return item;
  });
  localStorage.setItem("list", JSON.stringify(items));
}

// SETUP LOCALSTORAGE.REMOVEITEM('LIST');

// ****** setup items **********

function setupItems() {
  let items = getLocalStorage();

  if (items.length > 0) {
    items.forEach(function (item) {
      createListItem(item.id, item.value);
    });
    container.classList.add("show-container");
  }
}

function createListItem(id, value) {
  const element = document.createElement("article");
  let attr = document.createAttribute("data-id");
  attr.value = id;
  element.setAttributeNode(attr);
  element.classList.add("task-item");
  element.innerHTML = `<p class="title">${value}</p>
            <div class="Button-container">
              <!-- edit Button -->
              <button type="button" class="edit-button">
                <i class="fas fa-edit"></i>
              </button>
              <!-- delete Button -->
              <button type="button" class="delete-button">
                <i class="fas fa-trash"></i>
              </button>
            </div>`;
  // add event listeners to both buttons;
  const deleteButton = element.querySelector(".delete-button");
  deleteButton.addEventListener("click", deleteItem);
  const editButton = element.querySelector(".edit-button");
  editButton.addEventListener("click", editItem);

  // append child
  list.appendChild(element);
}
