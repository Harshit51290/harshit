function playGame(playerChoice) {
    const choices = ['rock', 'paper', 'scissors'];
    const computerChoice = choices[Math.floor(Math.random() * 3)];

    const result = determineWinner(playerChoice, computerChoice);

    displayResult(result, playerChoice, computerChoice);
}

function determineWinner(player, computer) {
    if (player === computer) return 'It\'s a tie!';
    
    if (
        (player === 'rock' && computer === 'scissors') ||
        (player === 'paper' && computer === 'rock') ||
        (player === 'scissors' && computer === 'paper')
    ) {
        return 'You win!';
    } else {
        return 'You lose!';
    }
}

function displayResult(result, playerChoice, computerChoice) {
    const resultText = document.getElementById('result-text');
    resultText.textContent = `${result} You chose ${playerChoice}, computer chose ${computerChoice}.`;
}function restartGame() {
    const resultText = document.getElementById('result-text');
    resultText.textContent = 'Choose your move!';
}

// Add this function at the end of the script.js file
function restartGame() {
    const resultText = document.getElementById('result-text');
    resultText.textContent = 'Choose your move!';
}