function interactiveText() {

    const interactiveTitle = document.querySelector('.interactiveTitle');
    let mouseX, mouseY;

    let traX, traY;
    document.addEventListener('mousemove', (e) => {
        mouseX = e.pageX;
        mouseY = e.pageY;
        traX = ((5 * mouseX) / 570) + 40;
        traY = ((5 * mouseY) / 570) + 40;

        interactiveTitle.style.backgroundPosition = `${traX}%  ${traY}% `;
    });
};
interactiveText();