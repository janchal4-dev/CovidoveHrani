const button0 = document.querySelector("#button0");
const diceDiv = document.querySelector("#diceDiv");
const playOnRow = document.querySelector("#playOnRow");
const player0ScoreInfo = document.querySelector("#player0ScoreInfo"); //celkové skóre hráčů
const player1ScoreInfo = document.querySelector("#player1ScoreInfo");
const whoWon = document.querySelector("#whoWon");
const player0WinInfo = document.querySelector("#player0WinInfo"); //absolutní počet výher, nikoliv celkového skóre
const player1WinInfo = document.querySelector("#player1WinInfo");



let playerNum = 0;
let player0Score = 0; 
let player1Score = 0;

let currentPlayer0Score = 0; 
let currentPlayer1Score = 0;

let player0WinNum = 0;
let player1WinNum = 0;

button0.addEventListener("click", function(){
    let diceNum = Math.ceil(Math.random() * 6);
    diceAdder(diceNum);
    playerNum = playerNum+1;
    if(playerNum % 2 == 0) {
        playOnRow.textContent = "Player 1 on the row";
        player1Score = player1Score + diceNum;
        player1ScoreInfo.textContent = player1Score; 

        currentPlayer1Score = diceNum

        if(currentPlayer0Score > currentPlayer1Score){
            whoWon.textContent = "Player 1 won";
            player0WinNum = player0WinNum + 1;
            player0WinInfo.textContent = player0WinNum;
        }
        else if(currentPlayer1Score > currentPlayer0Score){
            whoWon.textContent = "Player 2 won";
            player1WinNum = player1WinNum + 1;
            player1WinInfo.textContent = player1WinNum;
        }
        else if(currentPlayer1Score === currentPlayer0Score){
            whoWon.textContent = "Draw";
        }

         }
else {
    playOnRow.textContent = "Player 2 on the row";
    player0Score = player0Score + diceNum;
    player0ScoreInfo.textContent = player0Score; 

    currentPlayer0Score = diceNum;
    whoWon.textContent = "...";
    }

});

function diceAdder(num){
    diceDiv.style.backgroundImage=`url(img/cube${num}.png)`;
    diceDiv.style.color ="blue"
    console.log(num)
}