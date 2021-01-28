function burgerToggle() {
    const burgerIcon = document.querySelector('.header__burger');
    const burgerMenu = document.querySelector('.header__menu');
    const body = document.querySelector('body');

    burgerIcon.addEventListener('click', () => {
        burgerIcon.classList.toggle('active');
        burgerMenu.classList.toggle('active');
        body.classList.toggle('lock');
    })

    document.addEventListener('click', e => {

        if (e.target.classList.contains('header__link') && !e.target.classList.contains('productBtn')) {


            burgerIcon.classList.toggle('active');
            burgerMenu.classList.toggle('active');
            body.classList.toggle('lock');
        }
    });
};

function openProductMenu() {

    const productMenu = document.querySelector('.productMenu');
    const productBtn = document.querySelector('.productBtn');
    const containsSubMenu = document.querySelector('.containsSubMenu');
    const subMenuButton = containsSubMenu.querySelector('a');
    const subMenu = document.querySelector('.subMenu');


    productBtn.addEventListener('click', () => {
        productMenu.classList.toggle('showproductMenu');
    }, false);

    containsSubMenu.addEventListener('mouseenter', () => {

        if (document.documentElement.clientWidth > 767) {

            subMenu.classList.add('showproductMenu');

        };
    });

    document.addEventListener('click', e => {

        if (e.target !== productMenu && e.target !== productBtn && e.target !== subMenuButton) {


            productMenu.classList.remove('showproductMenu');
            subMenu.classList.remove('showproductMenu');
        }
    });

    containsSubMenu.addEventListener('click', () => {

        subMenu.classList.toggle('showproductMenu');
    });
};


function footerImagesShow() {
    const footerBlock = document.querySelector('#footerBlock');
    let i = 1;
    setInterval(() => {

        footerBlock.style.background = `url(/static/img/footerImage${i}.jpg) 0 0/cover no-repeat`;
        i === 5 ? i = 1 : ++i;
    }, 8000);
};






burgerToggle();
openProductMenu();
footerImagesShow();