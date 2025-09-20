from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.json.get('choice')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    result = determine_winner(player_choice, computer_choice)

    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result
    })

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        return "Player wins!"
    else:
        return "You lose, computer wins!"
    
if __name__ == '__main__':
    app.run(debug=True)