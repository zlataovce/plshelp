    const toggleClass =  (el, cls) => {
    if (Array.isArray(cls)) {
        cls.map((cl) => {
            el.classList.toggle(cl);
        });
    } else {
        el.classList.toggle(cls);
    }
};

function toggleTheme() {
    var footer = document.getElementById('footer')
    footer.classList.toggle("footer-dark")

    toggleClass(document.getElementById("navbar"), ['bg-dark', 'navbar-dark']);
    
    toggleClass(document.getElementById("body"), ['body-dark']);
    toggleClass(document.getElementById('darkmode'), ['body-dark']);
    toggleClass(document.getElementById('title'), ['title-dark']);
    toggleClass(document.getElementById("parse"), ['btn-primary']);
    toggleClass(document.getElementById('container'), ['container-dark']);
    toggleClass(document.getElementById('subtitle'), ['subtitle-dark']);
  }
