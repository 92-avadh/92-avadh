let userscore = 0;
let compscore = 0;

const choices = document.querySelectorAll('.choice');
const msag = document.querySelector(".message");
const user = document.querySelector("#user-board");
const comp = document.querySelector("#comp-board");

const drawgame = () =>{
    console.log("game was draw");
    msag.innerHTML = "game was draw! play agin.";
    msag.style.backgroundColor = "#081b31";
};

const showWinner =(userwin,userChoice,computerChoice)=>{
    if(userwin){
        console.log("you win");
        msag.innerHTML = `you win!your ${userChoice} beats ${computerChoice}.`;
        msag.style.backgroundColor = "green";
        userscore++;
        user.innerHTML = userscore;
    }else{
        console.log("you lose");
        msag.innerHTML = `you lose!your ${userChoice} beats ${computerChoice}.`;
        msag.style.backgroundColor = "red";
        compscore++;
        comp.innerHTML = compscore;

    }
};
const gencomputerchoice = () =>{
    let option =["rock","paper","scissors"];
    const randidx = Math.floor(Math.random()*3);
    return option[randidx];
};


const playgame = (userChoice) =>{
    console.log("user choices =",userChoice);
    const computerChoice = gencomputerchoice();
    console.log("computer choices =",computerChoice);
    if(userChoice === computerChoice){
     drawgame();   
    } else{
        let userwin = true;
        if(userChoice === "rock"){
           userwin = computerChoice === "paper" ? false : true;
        }
        else if(userChoice === "paper") {
          userwin = computerChoice === "scissors" ? false : true;
        }
        else(userChoice === "scissors")
         userwin = computerChoice === "rock" ? false : true;
        showWinner(userwin,userChoice,computerChoice);
    }
};


choices.forEach((choice) => 
    choice.addEventListener("click",() => {
        const userChoice = choice.getAttribute("id");
        playgame(userChoice);
    })
);

// function play(e) {
//     let playerChoice = e.target.id;
//     let computerChoice = getComputerChoice();
//     let winner = getWinner(playerChoice, computerChoice);
//     showWinner(winner, computerChoice);
// }