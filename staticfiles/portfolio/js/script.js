new Typed('#typing', {

    strings: [
        'Python Developer',
        'Django Developer',
        'Machine Learning Enthusiast',
        'Problem Solver'
    ],

    typeSpeed: 70,
    backSpeed: 50,
    loop: true
});

AOS.init({
    duration:1000
});

window.addEventListener('scroll', function(){

    const navbar = document.getElementById('navbar');

    if(window.scrollY > 50){
        navbar.classList.add('navbar-scrolled');
    }
    else{
        navbar.classList.remove('navbar-scrolled');
    }

});