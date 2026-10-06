const card = document.getElementById('card');
const cardContainer = document.querySelector('.card-container');

let targetX = 0, targetY = 0;
let currentX = 0, currentY = 0;
let animating = false;

function animateTilt() {
    currentX += (targetX - currentX) * 0.1;
    currentY += (targetY - currentY) * 0.1;
    card.style.transform = `
        perspective(1000px)
        rotateX(${currentX}deg)
        rotateY(${currentY}deg)
        translateZ(10px)
    `;
    animating = false;
}

document.addEventListener('mousemove', (event) => {
    const rect = cardContainer.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const deltaX = event.clientX - centerX;
    const deltaY = event.clientY - centerY;
    targetX = -(deltaY / 400);
    targetY = (deltaX / 400);
    if (!animating) {
        animating = true;
        requestAnimationFrame(animateTilt);
    }
});

document.addEventListener('mouseleave', () => {
    targetX = 0;
    targetY = 0;
    requestAnimationFrame(animateTilt);
});
