const second = document.querySelector('.second');
const third = document.querySelector('.third');
const fourth = document.querySelector('.fourth');

let maxScrollValue = document.body.offsetHeight - window.innerHeight;

document.addEventListener('scroll', function(){
    let current = window.pageYOffset
    let rate = current/maxScrollValue
    console.log(rate)
    if (rate > 0.11) {
        second.classList.remove("hide")
        second.classList.add("fade-in")
    }
    if (rate > 0.40) {
        third.classList.remove("hide")
        third.classList.add("fade-in")
    }
    if (rate > 0.72) {
        fourth.classList.remove("hide")
        fourth.classList.add("fade-in")
    }
})