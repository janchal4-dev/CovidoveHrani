/*
FCE načítající data z localStorage;
Ošetřit, pokud data v localStorage nejsou
*/

const getSavedNames = function(){
    const myNames = localStorage.getItem("names")

    if(myNames !==null){
        return JSON.parse(myNames)
    }
    else{
        return []
    }
}

/*
FCE pro použití při odeslání formuláře;
Ukládá do localStorage jméno z formuláře
*/

const saveNames = function(oneName0){
    localStorage.setItem("names", JSON.stringify(oneName0))

}


/*
    Generování HTML struktury, kterou umístíme do stránky po   kliknutí na tlačítko "Vypiš"
    + použijeme ji také pro vypsání nových informací z localStorage, když nějaké jméno vymažeme pomocí tlačítka "Vymazat jméno"
*/
const generateHtmlStructure = function(oneName1){
    const newDiv = document.createElement("div")
    newDiv.classList.add("newDiv")
    const newHref = document.createElement("a")
    const counterPar = document.createElement("p")
    const valueVarification = document.createElement("p")
    const button = document.createElement("button")
    const button2 = document.createElement("button")
    const input = document.createElement("input")
    input.style.width = "455px"
    input.setAttribute("id","editedName") 

    // nastavení mazacího tlačítka
    button.textContent = "Delete Task"
    newDiv.appendChild(button)
    newDiv.appendChild(document.createElement("br"));

    button2.textContent = "Edit Task"
    newDiv.appendChild(button2)
    newDiv.appendChild(document.createElement("br"));


    button.addEventListener("click", function(e){
    
        removeNames(names, oneName1.id) 
        saveNames(names)
        deleterAndRepeater(document.querySelector(".listNames"))
        
    })
    let number = 0

    button2.addEventListener("click", function(e){


        number = number + 1
        console.log(number)
        if(number % 2 == 0) {
            console.log("The number is even.");
            
            oneName1.firstName = input.value
            console.log(oneName1.firstName)

            let names = getSavedNames()
console.log(names)
let nameID = oneName1.id
let searchedName = names.find(function(oneObject){
    return oneObject.id === nameID
})

searchedName.firstName = input.value
saveNames(names)

           // saveNames(getSavedNames())
            input.remove()

             }
        else {
            console.log("The number is odd.")
            
            input.value = oneName1.firstName
            console.log(input.value)
            
            newHref.appendChild(input)

            const index = names.findIndex(function(nameWannaToCheck){
                return nameWannaToCheck.id === oneName1.id
            })
            console.log(oneName1.id)
            names.splice(index, 1)
        }
    })

   //  newHref.setAttribute("href", `edit.html#${oneName1.id}`)

    newHref.textContent = "Task: " + oneName1.firstName
    newDiv.appendChild(newHref)
    newDiv.appendChild(document.createElement("br"));
    newDiv.appendChild(document.createElement("br"));









    let datte = oneName1.deadline
    var d = new Date( datte );

if ( !!d.valueOf() ) {
    year = d.getFullYear();
    month = d.getMonth()+1;
    console.log(month)
    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    month = monthNames[month-1]



    //console.log(parseInt(month)+1)
    if(parseInt(month)<10){
        month = "0"+month
    }
    day = d.getDate();
    if(parseInt(day)<10){
        day = "0"+day
    }
    hour = d.getHours()
    if(parseInt(hour)<10){
        hour = "0"+hour
    }
    minute = d.getMinutes()
    if(parseInt(minute)<10){
        minute = "0"+minute
    }

let countDownDate = new Date(`${month} ${day}, ${year} ${hour}:${minute}:00 GMT+00:00`).getTime();

let x = setInterval(function() {
   
    // Získání dnešního data
    let now = new Date().getTime();
   
   //console.log(now)
   let distance = countDownDate - now;
        

   let days = Math.floor(distance / (1000 * 60 * 60 * 24));
   let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
   let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
   let seconds = Math.floor((distance % (1000 * 60)) / 1000);

           
    // Output s id="nextLesson"
    counterPar.innerHTML = "Deadline: " + days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";

}, 1000) ;

} 
else { 
 
}


newDiv.appendChild(counterPar)

  //  console.log(`Y: ${year} M: ${month} D: ${day} H: ${hour} Min: ${minute}`)














    if(oneName1.value === true){
        console.log(oneName1.firstName+" value")
        newDiv.classList.add("value")

    }
    else if(oneName1.value === false){
        console.log(oneName1.firstName+" Child")
        newDiv.classList.add("child")
    }
    
    return newDiv
}

// Podle ID najdeme index daného jména a pomocí splice ho odstraníme

const removeNames = function(ourNames, id){
    const index = ourNames.findIndex(function(nameWannaToCheck){
        return nameWannaToCheck.id === id
    })
    console.log(index)

    if(index >=0){
        ourNames.splice(index, 1)
    }
}
/*
Pokud smažeme nějaké jméno z localStorage, tak tato fce zabezpečí opětovné vypsání localStorage (tedy vypsání bez smazaného jména)
*/
// Moje verze

const deleterAndRepeater = function(div){
    div.innerHTML = ""
    getSavedNames()
    btnToList.click()

}

const nameDeleter = function(div){
    div.innerHTML = ""
}

// zjištění jestli není input empty - univerzální fce
const inputChecker = function(input, value){
    console.log(input)

    if (input > 0){
        //console.log("true")
        value = true
       // console.log(value)
        
    } 
    else if (input <= 0){
       // console.log("false")
        value = false
       // console.log(value)

    }
    console.log(value)
    return value
}
//fce na odškrtnutí checkboxu
const checkboxUn = function(checkbox){
  //  checkbox.checked = false
    
}

// fce na hledání pomocí id
const finderID = function(item, id){
let items = localStorage.getItem(item)
let myUser = JSON.parse(items)

let a = myUser.filter(function(b){
    let c = b.id.toLowerCase().includes(nameID)
    console.log(c)
    return c
    })
    return a
}

// fce na spuštění tlačítka a změnu stylů
const buttonSetFunction = function(btnID, style0, style1, click){
        document.querySelector(btnID).style.display ="block" 
        document.querySelector(style0).style.display ="block" 
        document.querySelector(style1).style.display ="none"  
    document.querySelector(btnID).addEventListener(click, function(e){
        //e.preventDefault()
        console.log("fce1")
        document.querySelector(style0).style.display ="none"
        document.querySelector(style1).style.display ="block"

    })
}
const styleChanger = function(style0, style1){
    document.querySelector(style0).style.display ="block"
    document.querySelector(style1).style.display ="none"
    document.querySelector(style0).textContent = searchedName.firstName
}


const click = function(object){
    document.querySelector(object).click()
    console.log("autoclick")
}

var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
if (isIOS) {
  document.querySelector("#dateInp").style.width ="465px"
} else {
    document.querySelector("#dateInp").style.width ="490px"
}