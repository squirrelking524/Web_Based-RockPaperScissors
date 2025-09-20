async function playGame(playerChoice) {
    const response = await fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ choice: playerChoice })
    });

    const data = await response.json();

    document.getElementById('player-choice-display').textContent = `You chose: ${data.player_choice}`;
    document.getElementById('computer-choice-display').textContent = `Computer chose: ${data.computer_choice}`;
    document.getElementById('game-result').textContent = data.result;
}