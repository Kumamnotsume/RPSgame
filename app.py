# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    emit('status', {'msg': f"{data['username']} has entered the room."}, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    emit('status', {'msg': f"{data['username']} has left the room."}, room=room)

@socketio.on('move')
def on_move(data):
    room = data['room']
    user_action = data['move']
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    result = determine_winner(user_action, computer_action)
    
    emit('result', {'user_action': user_action, 'computer_action': computer_action, 'result': result}, room=room)

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return "It's a tie!"
    elif user_action == "rock":
        return "You win!" if computer_action == "scissors" else "You lose!"
    elif user_action == "paper":
        return "You win!" if computer_action == "rock" else "You lose!"
    elif user_action == "scissors":
        return "You win!" if computer_action == "paper" else "You lose!"

if __name__ == '__main__':
    socketio.run(app, debug=True)
