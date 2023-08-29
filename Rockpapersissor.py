import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner of the game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle button click events
def play_game():
    player_choice = var.get()
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x500")  # Set window dimensions

# Available choices
choices = ["Rock", "Paper", "Scissors"]

# Create a variable to store the player's choice
var = tk.StringVar()

# Create a label
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg="pink", font=("Helvetica", 16))
label.pack(fill=tk.X)

# Create radio buttons for player's choice
for choice in choices:
    rb = tk.Radiobutton(root, text=choice, variable=var, value=choice, bg="green", font=("Helvetica", 14))
    rb.pack(fill=tk.X)

# Create a Play button
play_button = tk.Button(root, text="Play", command=play_game, bg="orange", font=("Helvetica", 14))
play_button.pack(fill=tk.X)

# Start the GUI main loop
root.mainloop()
