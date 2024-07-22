import random
import tkinter as tk

root = tk.Tk()
root.title("Rock Paper Scissors")
from PIL import Image

image = Image.open('C:/Users/steph/Documents/programming/myprograms/ImageLibrary/rock.ppm')
image.save('C:/Users/steph/Documents/programming/myprograms/ImageLibrary/rock.png')

image = Image.open('C:/Users/steph/Documents/programming/myprograms/ImageLibrary/paper.ppm')
image.save('C:/Users/steph/Documents/programming/myprograms/ImageLibrary/paper.png')

image = Image.open('C:/Users/steph/Documents/programming/myprograms/ImageLibrary/scissors.ppm')
image.save('C:/Users/steph/Documents/programming/myprograms/ImageLibrary/scissors.png')


# Load images
player_rock_photo = tk.PhotoImage(file='C:/Users/steph/Documents/programming/myprograms/ImageLibrary/rock.png')
player_paper_photo = tk.PhotoImage(file='C:/Users/steph/Documents/programming/myprograms/ImageLibrary/paper.png')
player_scissors_photo = tk.PhotoImage(file='C:/Users/steph/Documents/programming/myprograms/ImageLibrary/scissors.png')

#Load images for computer


computer_rock_photo = tk.PhotoImage(file='C:/Users/steph/Documents/programming/myprograms/ImageLibrary2/rock.png')
computer_paper_photo = tk.PhotoImage(file='C:/Users/steph/Documents/programming/myprograms/ImageLibrary2/paper.png')
computer_scissors_photo = tk.PhotoImage(file='C:/Users/steph/Documents/programming/myprograms/ImageLibrary2/scissors.png')

def determine_winner(user_action, computer_action):

    if user_action == computer_action:
        return "It's a tie!"
    elif user_action == "rock":
        return "You win!" if computer_action == "scissors" else "You lose!"
    elif user_action == "paper":
        return "You win!" if computer_action == "rock" else "You lose!"
    elif user_action == "scissors":
        return "You win!" if computer_action == "paper" else "You lose!"

def on_choice(user_action):
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    
    result_text = determine_winner(user_action, computer_action)
    result_label.config(text=result_text)

#Computers choice display

    if computer_action == "rock":
        computer_choice_label.config(image=computer_rock_photo)
    elif computer_action == "paper":
        computer_choice_label.config(image=computer_paper_photo)
    elif computer_action == "scissors":
        computer_choice_label.config(image=computer_scissors_photo)
    

# Buttons for images
rock_button = tk.Button(root, image=player_rock_photo, command=lambda: on_choice("rock"))
paper_button = tk.Button(root, image=player_paper_photo, command=lambda: on_choice("paper"))
scissors_button = tk.Button(root, image=player_scissors_photo, command=lambda: on_choice("scissors"))

rock_button.pack(side="left")
paper_button.pack(side="left")
scissors_button.pack(side="left")

# Label to display results
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

#Label to display computer results
computer_choice_label = tk.Label(root)
computer_choice_label.pack()


root.mainloop()
