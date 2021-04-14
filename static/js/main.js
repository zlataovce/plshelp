const toggleClass =  (el, cls) => {
    if (Array.isArray(cls)) {
        cls.map((cl) => {
            if (el !== null) {
              el.classList.toggle(cl);
            }
        });
    } else {
        if (el !== null) {
          el.classList.toggle(cls);
        }
    }
};

function DarkModeIndex() {
    if (localStorage.getItem("theme") === "dark") {
        localStorage.setItem("theme", "light");
    } else if (localStorage.getItem("theme") === "light") {
        localStorage.setItem("theme", "dark");
    }
    var footer = document.getElementById("footer");
    footer.classList.toggle("footer-dark");

    toggleClass(document.getElementById("navbar"), ["bg-dark", "navbar-dark"]);

    toggleClass(document.getElementById("body"), ["body-dark"]);
    toggleClass(document.getElementById("title"), ["title-dark"]);
    toggleClass(document.getElementById("parse"), ["btn-primary"]);
    // toggleClass(document.getElementById("container"), ["container-dark"]);
    toggleClass(document.getElementById("subtitle"), ["subtitle-dark"]);
  }


function DarkModeShow() {
    if (localStorage.getItem("theme") === "dark") {
        localStorage.setItem("theme", "light");
    } else if (localStorage.getItem("theme") === "light") {
        localStorage.setItem("theme", "dark");
    }
    var footer = document.getElementById("footer");
    footer.classList.toggle("footer-dark");

    toggleClass(document.getElementById("navbar"), ["bg-dark", "navbar-dark"]);
    toggleClass(document.getElementById("info1"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info2"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info3"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info4"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info5"), ["subtitle-dark"]);
    toggleClass(document.getElementById("error"), ["monospace-dark"]);
    toggleClass(document.getElementById("body"), ["body-dark"]);
    toggleClass(document.getElementById("spacer"), ["body-dark"]);
    toggleClass(document.getElementById("title"), ["title-dark"]);
    toggleClass(document.getElementById("title2"), ["title-dark2"]);
    toggleClass(document.getElementById("card1"), ["card-dark"]);
    toggleClass(document.getElementById("card2"), ["card-dark"]);
    toggleClass(document.getElementById("card3"), ["card-dark"]);
    toggleClass(document.getElementById("card4"), ["card-dark"]);
    toggleClass(document.getElementById("card5"), ["card-dark"]);
    toggleClass(document.getElementById("smalltitle"), ["subtitle-dark"]);
}

$(document).ready(function WindowLoad(event) {
    if (localStorage.getItem("theme") === null) {
        localStorage.setItem("theme", "dark");  // Change this to light if you want the light mode as default
    }

    if (localStorage.getItem("theme") === "dark") {
        var footer = document.getElementById("footer");
        footer.classList.toggle("footer-dark");
        if (window.location.pathname === "/") {
            toggleClass(document.getElementById("navbar"), ["bg-dark", "navbar-dark"]);
            toggleClass(document.getElementById("body"), ["body-dark"]);
            toggleClass(document.getElementById("title"), ["title-dark"]);
            toggleClass(document.getElementById("parse"), ["btn-primary"]);
            // toggleClass(document.getElementById("container"), ["container-dark"]);
            toggleClass(document.getElementById("subtitle"), ["subtitle-dark"]);
        } else {
            toggleClass(document.getElementById("navbar"), ["bg-dark", "navbar-dark"]);
            toggleClass(document.getElementById("info1"), ["subtitle-dark"]);
            toggleClass(document.getElementById("info2"), ["subtitle-dark"]);
            toggleClass(document.getElementById("info3"), ["subtitle-dark"]);
            toggleClass(document.getElementById("info4"), ["subtitle-dark"]);
            toggleClass(document.getElementById("info5"), ["subtitle-dark"]);
            toggleClass(document.getElementById("error"), ["monospace-dark"]);
            toggleClass(document.getElementById("body"), ["body-dark"]);
            toggleClass(document.getElementById("spacer"), ["body-dark"]);
            toggleClass(document.getElementById("title"), ["title-dark"]);
            toggleClass(document.getElementById("title2"), ["title-dark2"]);
            toggleClass(document.getElementById("card1"), ["card-dark"]);
            toggleClass(document.getElementById("card2"), ["card-dark"]);
            toggleClass(document.getElementById("card3"), ["card-dark"]);
            toggleClass(document.getElementById("card4"), ["card-dark"]);
            toggleClass(document.getElementById("card5"), ["card-dark"]);
            toggleClass(document.getElementById("card6"), ["card-dark"]);
            toggleClass(document.getElementById("smalltitle"), ["subtitle-dark"]);
        }
    }
});

function copyToClipboard(element) {
  var $temp = $("<input>");
  $("body").append($temp);
  $temp.val($(element).text()).select();
  document.execCommand("copy");
  $temp.remove();
}

function toggleVisibility(element, titlelem) {
  if (titlelem.innerHTML.includes("⯆")) {
    titlelem.innerHTML = titlelem.innerHTML.replace("⯆", "⯈");
  } else {
    titlelem.innerHTML = titlelem.innerHTML.replace("⯈", "⯆");
  }
  toggleClass(document.getElementById(element), ["d-none"]);
}

function toggleviewMode(button, simple, advanced) {
  toggleClass(document.getElementById(simple), ["d-none"]);
  toggleClass(document.getElementById(advanced), ["d-none"]);
  if (button.innerHTML.includes("Simple mode")) {
    button.innerHTML = button.innerHTML.replace("Simple mode", "Advanced mode");
  } else {
    button.innerHTML = button.innerHTML.replace("Advanced mode", "Simple mode");
  }
}
