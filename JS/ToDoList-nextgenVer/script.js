/*
Načtení data z localStorage do proměnné names; pokud je localStorage prázdný, tak do names se uloží prázdné pole
*/
const names = getSavedNames()

/*
Odeslání formuláře a uložení do localstorage pomocí proměnné names
*/

let form0 = document.querySelector("#form0")




form0.addEventListener("submit", function(e){
    e.preventDefault()
    

    let asdf = e.target.elements.firstName.value.replace(/\s/g,'').length

//console.log(e.target.elements.firstName.value.length+1)

const inputChecker0 = inputChecker(asdf, "hhi")
console.log(inputChecker0)
if(inputChecker0 === true){
    console.log("Input checker true")
        names.push({
        id: uuidv4(),
        firstName: e.target.elements.firstName.value,
        deadline: e.target.elements.deadline.value,
    })
    

}
else if(inputChecker0 === false){
    console.log("Input checker false")
}

   

    e.target.elements.firstName.value = ""
    saveNames(names)
    document.querySelector(".toList").click()
})

//vypisování zpět do stránky
let btnToList = document.querySelector(".toList")
btnToList.addEventListener("click", function(e){

    nameDeleter(document.querySelector(".listNames"))

    let namesFromLocalStorrage = localStorage.getItem("names")
    let namesFromLocalStorrageJSON = JSON.parse(namesFromLocalStorrage)

   //console.log(namesFromLocalStorrageJSON)

    namesFromLocalStorrageJSON.forEach(function(myName){
        const oneNameHtml = generateHtmlStructure(myName)
        document.querySelector(".listNames").appendChild(oneNameHtml)
    
    })

})
click(".toList")

window.addEventListener("storage", function(){
    location.reload()
    click(".toList")
})





//zakomentovat pak
//btnToList.click()

