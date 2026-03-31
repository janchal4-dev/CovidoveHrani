let nameID = location.hash.substring(1)
//console.log(nameID)
let names = getSavedNames()
console.log(names)


let searchedName = names.find(function(oneObject){
    return oneObject.id === nameID
})

console.log(searchedName)

if(searchedName === undefined){
    location.assign("index.html")
    console.log("wieb")
}
let finder = finderID("names")
console.log(finder)

document.querySelector("#nameHeader").textContent = searchedName.firstName
document.querySelector("#editedName").value = searchedName.firstName
document.querySelector("#editedCheckbox").checked  = searchedName.adult


//searchedName.adult = ""

let number = 0

let changingForm = document.querySelector("#changing-form")
changingForm.addEventListener("submit", function(e){
    e.preventDefault()

    searchedName.firstName = e.target.elements.changingName.value
    searchedName.adult = e.target.elements.changingCheckbox.checked

    saveNames(names)

    //buttonSetFunction("#changing-form",  "#editedName", "#nameHeader")

   //buttonSetFunction1("#changing-form", "#editedName", "#nameHeader", "submit")
   

   console.log("fce2")
   
   number++
   if(number % 2 == 0) {
    console.log("The number is even.");
    styleChanger("#nameHeader", "#editedName")
     }
else {
    console.log("The number is odd.");
}

})

buttonSetFunction("#nameHeader", "#nameHeader", "#editedName" , "click")

document.querySelector("#indexHref").addEventListener("click", function(e){
    window.location.href = 'index.html';
})

/*

let changingForm = document.querySelector("#changing-form")
changingForm.addEventListener("submit", function(event){
    event.preventDefault()
 
    searchedName.firstName = event.target.elements.changingName.value
 
    saveNames(names)
})



let changingForm = document.querySelector("#changing-form")
changingForm.addEventListener("submit", function(e){
    e.preventDefault()

    console.log(e.target.elements.changingName.value)
    //searchedName.firstName = e.target.elements.changingName.value

    saveNames(names)
    console.log("wbc")
})




*/
/*window.addEventListener("click", function(){
    console.log("Bylo kliknuto")
})
*/

window.addEventListener("storage", function(e){
    console.log(e)

    if(e.key === "names"){
        names = JSON.parse(e.newValue)
    }

    let searchedName = names.find(function(oneObject){
        return oneObject.id === nameID
    })
    
    console.log(searchedName)
    
    if(searchedName === undefined){
        location.assign("index.html")
        console.log("wieb")
    }
    let finder = finderID("names")
    console.log(finder)
    
    document.querySelector("#nameHeader").textContent = searchedName.firstName
    document.querySelector("#editedName").value = searchedName.firstName
    document.querySelector("#editedCheckbox").checked  = searchedName.adult

})
