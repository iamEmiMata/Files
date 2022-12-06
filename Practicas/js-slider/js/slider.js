
//  Slider 

let onSlide = false;

window.addEventListener("load", () => {
   autoSlide();

   const dots = document.querySelectorAll(".dot");
   for (let i = 0; i < dots.length; i++) {
      dots[i].addEventListener("click", () => slide(i));
   }

   const buttonPrev = document.querySelector(".prev");
   const buttonNext = document.querySelector(".next");
   buttonPrev.addEventListener("click", () => slide(getItemActiveIndex() - 1));
   buttonNext.addEventListener("click", () => slide(getItemActiveIndex() + 1));
})

function autoSlide() {
   setInterval(() => {
      slide(getItemActiveIndex() + 1);
   }, 5000); // slide speed = 4.5s
}

function slide(toIndex) {
   if (onSlide)
      return;
   onSlide = true;

   const itemsArray = Array.from(document.querySelectorAll(".item"));
   const itemActive = document.querySelector(".active-item");
   const itemActiveIndex = itemsArray.indexOf(itemActive);
   let newItemActive = null;

   if (toIndex > itemActiveIndex) {
      // check if toIndex exceeds the number of carousel items
      if (toIndex >= itemsArray.length) {
         toIndex = 0;
      }

      newItemActive = itemsArray[toIndex];

      // start transition
      newItemActive.classList.add("prev-slide-img");
      setTimeout(() => {
         newItemActive.classList.add("prev-img");
         itemActive.classList.add("prev-img");
      }, 20);
   } else {
      // check if toIndex exceeds the number of carousel items
      if (toIndex < 0) {
         toIndex = itemsArray.length - 1;
      }

      newItemActive = itemsArray[toIndex];

      // start transition
      newItemActive.classList.add("next-slide-img");
      setTimeout(() => {
         newItemActive.classList.add("next-img");
         itemActive.classList.add("next-img");
      }, 20);
   }

   // remove all transition class and switch active class
   newItemActive.addEventListener("transitionend", () => {
      itemActive.className = "item";
      newItemActive.className = "item active-item";
      onSlide = false;
   }, {
      once: true
   });

   slideIndicator(toIndex);
}

function getItemActiveIndex() {
   const itemsArray = Array.from(document.querySelectorAll(".item"));
   const itemActive = document.querySelector(".active-item");
   const itemActiveIndex = itemsArray.indexOf(itemActive);
   return itemActiveIndex;
}

function slideIndicator(toIndex) {
   const dots = document.querySelectorAll(".dot");
   const dotActive = document.querySelector(".active-dot");
   const newDotActive = dots[toIndex];

   dotActive.classList.remove("active-dot");
   newDotActive.classList.add("active-dot");
}