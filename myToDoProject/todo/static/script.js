// Variables
const addTextBox = document.querySelector("#addTextBox");
const addButton = document.querySelector("#addButton");
const ul = document.querySelector(".row2 ul");
const deleteBtns = document.querySelectorAll(".deleteBtn");
const editBtns = document.querySelectorAll(".fa-pen-to-square");

console.log(
  "♡ Jó napot! Welcome to my to-do app! Made using Python's Django ♡"
);

// ---------------------------------------------------------------- //

// The delete button
function addDeleteListener(deleteBtn) {
  deleteBtn.addEventListener("click", function () {
    var controlsDiv = this.parentNode;
    var liElement = controlsDiv.parentNode;

    liElement.remove();
  });
}

// The edit button
function addEditListener(editBtn) {
  editBtn.addEventListener("click", function () {
    var controlsDiv = this.parentNode;
    var liElement = controlsDiv.parentNode;
    var p = liElement.querySelector("p");

    var textInside = p.textContent;

    p.remove();

    var textBox = document.createElement("input");
    textBox.type = "text";
    textBox.value = textInside;
    textBox.classList.add("inputBox");
    liElement.prepend(textBox); 

    textBox.addEventListener("keydown", (event) => {
      if (event.keyCode === 13 || event.key === "Enter") {

        textInside = textBox.value;
        textBox.remove();
        var p = document.createElement("p");
        p.textContent = textInside;

        liElement.prepend(p); 
      }
    });
  });
}

// Function to the add button to the textbox
addButton.addEventListener("click", function () {
  let text = addTextBox.value;

  addTextBox.value = "";

  let li = document.createElement("li");
  let p = document.createElement("p");

  p.textContent = text;
  let controls = `<div class="controls">
        <i class="fa-regular fa-pen-to-square"></i>
        <i class="deleteBtn fa-regular fa-trash-can"></i>
      </div>`;

  li.innerHTML = p.outerHTML + controls;

  ul.appendChild(li);

  const deleteBtns = li.querySelectorAll(".deleteBtn");
  const editBtns = li.querySelectorAll(".fa-pen-to-square");

  deleteBtns.forEach(function (deleteBtn) {
    addDeleteListener(deleteBtn);
  });

  editBtns.forEach(function (editBtn) {
    addEditListener(editBtn);
  });
});

// The delete and edit button functions for list items already there
deleteBtns.forEach(function (deleteBtn) {
  addDeleteListener(deleteBtn);
});

editBtns.forEach(function (editBtn) {
  addEditListener(editBtn);
});

// Constantly count how many li elements there are
setInterval(function () {
  var liCount = ul.getElementsByTagName("li").length;

  // if above 10 items, disable the button
  if (liCount > 10) {
    addButton.classList.add("disabled-btn");
    addButton.disabled = true;
  }
  // if below 10 items, enable the button
  else if (liCount < 11) {
    addButton.classList.remove("disabled-btn");
    addButton.disabled = false;
  }
}, 1000); // every second!
