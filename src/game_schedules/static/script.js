const dialog = document.querySelector("dialog");
const showButton = document.querySelector("#newLocation");
const closeButton = document.querySelector("dialog button");
console.log("querySelector12", showButton);

showButton.addEventListener("click", () => {
  dialog.showModal();
});

// "Close" button closes the dialog
closeButton.addEventListener("click", () => {
  dialog.close();
});
