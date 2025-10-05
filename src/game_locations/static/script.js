// dialog not implemented but holding on to make it work
//
// const dialog = document.querySelector("dialog");
// const showButton = document.querySelector("#newLocation");
// const closeButton = document.querySelector("dialog button");

// showButton.addEventListener("click", () => {
//   dialog.showModal();
// });

// // "Close" button closes the dialog
// closeButton.addEventListener("click", () => {
//   dialog.close();
// });

const searchBox = document.getElementById("searchBox");
const locationList = document.getElementById("venue-list");
const locations = locationList.getElementsByTagName("li");

searchBox.addEventListener("keyup", () => {
  const filterKey = searchBox.value.toLowerCase();

  for (let i = 0; i < locations.length; i++) {
    const text = locations[i].textContent.toLowerCase().trim().split(/\s+/);
    const hasSomeMatch = text.some((x) => x.includes(filterKey));

    if (hasSomeMatch) {
      locations[i].style.display = "";
    } else {
      locations[i].style.display = "none";
    }
  }
});

const resetButton = document.getElementById(
  "storedLocation_searchAction-reset",
);
resetButton.addEventListener("click", () => {
  searchBox.value = "";
  searchBox.dispatchEvent(new Event("keyup"));
});
