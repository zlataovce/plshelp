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
    var footer = document.getElementById("footer");
    footer.classList.toggle("footer-dark");

    toggleClass(document.getElementById("navbar"), ["bg-dark", "navbar-dark"]);

    toggleClass(document.getElementById("body"), ["body-dark"]);
    toggleClass(document.getElementById("darkmode"), ["body-dark"]);
    toggleClass(document.getElementById("title"), ["title-dark"]);
    toggleClass(document.getElementById("parse"), ["btn-primary"]);
    toggleClass(document.getElementById("container"), ["container-dark"]);
    toggleClass(document.getElementById("subtitle"), ["subtitle-dark"]);
  }


function DarkModeShow() {
    var footer = document.getElementById("footer");
    footer.classList.toggle("footer-dark");

    toggleClass(document.getElementById("navbar"), ["bg-dark", "navbar-dark"]);
    toggleClass(document.getElementById("info1"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info2"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info3"), ["subtitle-dark"]);
    toggleClass(document.getElementById("info4"), ["subtitle-dark"]);
    toggleClass(document.getElementById("error"), ["error-dark"]);
    toggleClass(document.getElementById("body"), ["body-dark"]);
    toggleClass(document.getElementById("spacer"), ["body-dark"]);
    toggleClass(document.getElementById("title"), ["title-dark"]);
    if (document.getElementById("card1") !== null) {
      document.getElementById("card1").style.color = "#FFFFFF";
      document.getElementById("card1").style.backgroundColor = "#36393f";
    }
    if (document.getElementById("card2") !== null) {
      document.getElementById("card2").style.color = "#FFFFFF";
      document.getElementById("card2").style.backgroundColor = "#36393f";
    }
    if (document.getElementById("card3") !== null) {
      document.getElementById("card3").style.color = "#FFFFFF";
      document.getElementById("card3").style.backgroundColor = "#36393f";
    }
    if (document.getElementById("card4") !== null) {
      document.getElementById("card4").style.color = "#FFFFFF";
      document.getElementById("card4").style.backgroundColor = "#36393f";
    }
    if (document.getElementById("card5") !== null) {
      document.getElementById("card5").style.color = "#FFFFFF";
      document.getElementById("card5").style.backgroundColor = "#36393f";
    }
}
