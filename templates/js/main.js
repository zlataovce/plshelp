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

    toggleClass(document.getElementById('navbar'), ['bg-dark', 'navbar-dark']);
  }

