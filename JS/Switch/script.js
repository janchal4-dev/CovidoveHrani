document.getElementsByTagName('.slider::before')[0].style.backgroundColor = 'RED';
function change(){
    let lightDark = document.getElementById(`light-text`)
    if (lightDark.innerHTML === "Light"){
        lightDark.innerHTML = "Dark"
        }
    else{
        lightDark.innerHTML = "Light"
    }
    let body = document.body;
    body.classList.toggle("lights-on")
    let slider = document.span;
    slider.classList.toggle(".slider::after")
}