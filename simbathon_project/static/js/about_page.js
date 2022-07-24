const one = document.querySelector(".about_first");
const two = document.querySelector(".about_posting_info_p_first");
const three = document.querySelector(".about_posting_info_p_second");
const four = document.querySelector(".about_posting_info_p_thrid");
const five = document.querySelector(".about_posting_info_p_last");
const six = document.querySelector(".about_us_profile_t");
const seven = document.querySelector(".about_DD");
const eight = document.querySelector(".about_FE");
const nine = document.querySelector(".about_BE");
const ten = document.querySelector(".about_divider");
const a = document.querySelector(".about_github_page");



let maxScrollValue = document.body.offsetHeight - window.innerHeight;

document.addEventListener('scroll', function(){
    let current = window.pageYOffset
    let rate = current/maxScrollValue
    console.log(rate);
    if (rate > 0.005) {
        one.classList.remove("hideen")
        one.classList.add("about_first_title_fade_in")
    }
    if (rate > 0.05) {
        two.classList.remove("hideen")
        two.classList.add("about_slide_left")
    }
    if (rate > 0.17) {
        three.classList.remove("hideen")
        three.classList.add("about_slide_right")
    }
    if (rate > 0.29) {
        four.classList.remove("hideen")
        four.classList.add("about_slide_left")
    }
    if (rate > 0.42) {
        five.classList.remove("hideen")
        five.classList.add("about_first_title_fade_in")
    }
    if (rate > 0.48) {
        ten.classList.remove("hideen")
        ten.classList.add("about_first_title_fade_in")
    }
    if(rate > 0.55){
        six.classList.remove("hideen")
        six.classList.add("about_first_title_fade_in")
    }
    if(rate > 0.64){
        seven.classList.remove("hideen")
        seven.classList.add("about_slide_left")
    }
    if(rate > 0.75){
        eight.classList.remove("hideen")
        eight.classList.add("about_slide_left")
    }
    if(rate > 0.9){
        nine.classList.remove("hideen")
        nine.classList.add("about_slide_left")
        a.classList.remove("hideen")
        a.classList.add("about_first_title_fade_in")
    }
})