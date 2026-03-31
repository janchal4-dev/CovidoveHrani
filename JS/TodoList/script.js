window.onload = function(){
    let button = document.querySelector(".toList");
    button.click();
}



let form0 = document.querySelector("#form0")
let taskNumber = 0

//odstranit od
/*let userFromJS1 = localStorage.getItem("criminals")
            //převedení zpět na pole
            let myUser1 = JSON.parse(userFromJS1)
            console.log(myUser1)
/*Odstranit do */
// Current time
let todayTime = new Date()
let time = `${todayTime.getHours()}:${todayTime.getMinutes()}:${todayTime.getSeconds()}` 
if(todayTime.getMinutes() >10 && todayTime.getSeconds() > 10){
    time = `${todayTime.getHours()}:0${todayTime.getMinutes()}:0${todayTime.getSeconds()}`
}
else if(todayTime.getMinutes()){
    time = `${todayTime.getHours()}:0${todayTime.getMinutes()}:${todayTime.getSeconds()}` 
}
else if(todayTime.getSeconds()){
    time = `${todayTime.getHours()}:${todayTime.getMinutes()}:0${todayTime.getSeconds()}` 
}
// Current date
let todayDate = new Date()
let date = `${(todayDate.getMonth()+1)}-${todayDate.getDate()}-${todayDate.getFullYear()}`

let myArray
if(localStorage.getItem("criminals") === null){
    myArray = []

    const warnDiv = document.createElement("div")
    warnDiv.classList.add("div1")
    document.querySelector("#div0").appendChild(warnDiv)

    const warnPar = document.createElement("p")
    warnPar.textContent = "To do list is empty :)"
    warnDiv.appendChild(warnPar)
}
else{
    myArray = JSON.parse(localStorage.getItem("criminals"))
}
let control = 0

form0.addEventListener("submit", function(event){
    //event.preventDefault()
    let task = event.target.elements.task.value
    let deadline = event.target.elements.deadline.value
    if(task !== "" || deadline !== ""){
    myArray.push({
        id: "",
        task: task,
        deadline: deadline,
    })
    console.log("weighf")
    window.onload = function(){
        document.querySelector(".toList").click();
        location.reload();
    }
    }
    else{
       // alert("Would you be so kind and send only Array with text.")
       window.onload = function(){
        document.querySelector(".toList").click();
        location.reload();
    }
    }
    myArrayJson = JSON.stringify(myArray)
    localStorage.setItem("criminals", myArrayJson)
})

let JsonClear = document.querySelector("#JsonClear")
JsonClear.addEventListener("click", function(){
    localStorage.clear()
    console.log(`LocalStorage has been cleared in ${date} in the time of ${time} `)
    setTimeout(function () {
       location.reload()
        
    }, 0000); //časovač je vypnutý
})
/*
let div0 = document.querySelector("#div0")
*/

let count = 0
let toList = document.querySelector(".toList")
toList.addEventListener("click", function(){
    let myStorage = localStorage.getItem("criminals")
    let myStorageJSON = JSON.parse(myStorage)

    count = count+1
    console.log(count)

    //console.log(myStorageJSON)
    if (myStorageJSON !== null){
        if(count>1){
            document.querySelector("#div0").innerHTML = ""         
        }
for(let i=0; i < myStorageJSON.length; i++){
  
        
        div1 = document.createElement("div")
        div1.classList.add("div1")
        document.querySelector("#div0").appendChild(div1)
       
        let countDownDate = new Date(myStorageJSON[i].deadline).getTime();

        let now = new Date().getTime();
   
        
 
        let distance = countDownDate - now;
console.log(now)
console.log(countDownDate)

        let days = Math.floor(distance / (1000 * 60 * 60 * 24));
    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        

        console.log(myStorageJSON[i])
        let p0 = document.createElement("p")
        p0.innerHTML = 
        `Task: ${myStorageJSON[i].task} <br>
        Deadline: ${myStorageJSON[i].deadline} (${days + "d " + hours + "h "
        + minutes + "m " + seconds + "s "} left)`
        div1.appendChild(p0)

        let checkBox = document.createElement("INPUT")
        checkBox.setAttribute("type", "checkbox")
        checkBox.classList.add("checkbox")

        let p1 = document.createElement("p")
        p1.textContent = "Done"
        div1.appendChild(p1)
        p1.classList.add("doneP")
        div1.appendChild(checkBox)

        let p2 = document.createElement("p")
        p2.textContent = " "
        div1.appendChild(p2)

        let button0 = document.createElement("button")
        button0.innerHTML = "Delete"
        button0.classList.add("button0")
        div1.appendChild(button0)

        let button1 = document.createElement("button")
        button1.innerHTML = "Delete from LocalStorage"
        button1.classList.add("button1")
        div1.appendChild(button1)


        taskNumber++
        console.log(taskNumber)

     if(document.querySelector(".button1") !== null){
            button1.addEventListener("click", function(e){
                let userFromJS = localStorage.getItem("criminals")
            //převedení zpět na pole
            let myUser = JSON.parse(userFromJS)
           myUser.splice(i,1)
           //myUser.splice(1,2)
            console.log(myUser)
            console.log(i)
            localStorage.clear();

            myArrayJson = JSON.stringify(myUser)
    localStorage.setItem("criminals", myArrayJson) 
    location.reload()
           
                
            })
         }

       /* let p3 = document.createElement("p")
        p3.textContent = "-----------------------------------------"
        div1.appendChild(p3)*/
        button0.addEventListener("click", function(){
            p0.remove()
            p1.remove()
            p2.remove()
          //  p3.remove()
            button0.remove()
            checkBox.remove()
            document.querySelector(".div1").remove()
        })
    }
    }
})
