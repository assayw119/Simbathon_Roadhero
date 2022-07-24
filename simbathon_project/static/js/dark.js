const toggle = document.getElementById("toggle_btn");
const body = document.querySelector('body');

toggle.addEventListener("click", function(){
    if (!body.classList.contains('lightmode')) {
        body.classList.add('lightmode');
        toggle.classList.remove('fa-moon');
        toggle.classList.add('fa-sun');
        localStorage.setItem('whatMode', 'lightmode');
   }
      else {
        body.classList.remove('lightmode');
        toggle.classList.remove('fa-sun');
        toggle.classList.add('fa-moon');
        localStorage.setItem('whatMode', 'darkmode');
      }
})

document.addEventListener('DOMContentLoaded',function(){
    const whatMode = localStorage.getItem('whatMode');
    if (whatMode === "darkmode") {
        body.classList.remove('lightmode');
        toggle.classList.remove('fa-sun');
        toggle.classList.add('fa-moon');
      }  
    else {
        body.classList.add('lightmode');
        toggle.classList.remove('fa-moon');
        toggle.classList.add('fa-sun');
       }
})