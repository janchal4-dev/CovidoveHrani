// 'use strict';
const icon = document.querySelector("#icon")
const input0 = document.querySelector(".input0")
const result = document.querySelector("p")

let count0 = 0
icon.addEventListener("click", function(e){
    e.preventDefault()
    inputLeftRigth()

})



//fce na vypsání do html kódu, co bylo v imputu
function resultWriter(result, input){
    result.textContent = input.value
}


//fce na input 
function inputLeftRigth(){
    count0++

    if(count0 % 2 == 0) {
    input0.classList.remove("after") 
    input0.classList.add("before") 
    input0.style.backgroundColor = "white"
    // console.log(input0.value.length)
    if(input0.value.length > 0){
    resultWriter(result, input0)
    }
}
    else{
    input0.classList.remove("before") 
    input0.classList.add("after") 
    input0.value=""
    }

    input0.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            input0.classList.remove("after") 
            input0.classList.add("before") 
            input0.style.backgroundColor = "white"
            // console.log(input0.value.length)
            if(input0.value.length > 0){
            resultWriter(result, input0)
            }}
        })
   
input0.addEventListener('keydown', function(event){
	if(event.key === `Escape`){
		input0.classList.remove("after") 
            input0.classList.add("before") 
            input0.style.backgroundColor = "white"
            input0.value = result.textContent

	}
})
}
