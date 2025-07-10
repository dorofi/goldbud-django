const navToggle = document.querySelector('.nav-toggle');
const navWrapper = document.querySelector('.nav-wrapper');

navToggle.addEventListener('click', () => {
    // This will toggle the visibility of the navigation menu
    navWrapper.classList.toggle('active');
    // This can be used to animate the hamburger icon itself (e.g., to an 'X')
    navToggle.classList.toggle('active');
});