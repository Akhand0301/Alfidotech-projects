"""
Task:- 
Create a Number Guessing Game

Objective:- 
Develop a command-line game where the computer randomly selects a number, 
and the user has to guess it

Features:- 
Generate a random number between 1 and 100.
Allow the user to input guesses and provide feedback on whether the guess is too high, too low, or correct.
Track the number of attempts and display it when the user guesses correctly.

Technologies:-
Python basics (loops, conditionals, random module).

"""

#_______________My_code_________________________________

import random
import tkinter as tk
from tkinter import messagebox

# Function to handle the number guessing game logic
def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    def check_guess():
        nonlocal attempts
        try:
            user_guess = int(entry_guess.get())  # Get the user's guess from the input field
            attempts += 1
            
            # Check the guess and provide feedback
            if user_guess < secret_number:
                label_feedback.config(text="Too low! Try again.", fg="blue")
            elif user_guess > secret_number:
                label_feedback.config(text="Too high! Try again.", fg="blue")
            else:
                label_feedback.config(text=f"Congratulations! You've guessed the correct number: {secret_number}", fg="green")
                label_attempts.config(text=f"It took you {attempts} attempts.")
                button_guess.config(state="disabled")  # Disable the guess button after correct guess
        except ValueError:
            # Handle invalid input
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 100.")
    
    # Set up the main window
    window = tk.Tk()
    window.title("Number Guessing Game")
    window.geometry("400x300")  # Set the size of the window

    # Welcome label
    label_welcome = tk.Label(window, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
    label_welcome.pack(pady=10)

    # Instructions label
    label_instructions = tk.Label(window, text="Guess a number between 1 and 100:", font=("Arial", 12))
    label_instructions.pack(pady=5)

    # Input field for user guess
    entry_guess = tk.Entry(window, font=("Arial", 12))
    entry_guess.pack(pady=5)

    # Button to submit guess
    button_guess = tk.Button(window, text="Guess", font=("Arial", 12), command=check_guess)
    button_guess.pack(pady=10)

    # Feedback label to show results of the guess
    label_feedback = tk.Label(window, text="", font=("Arial", 12), fg="black")
    label_feedback.pack(pady=5)

    # Label to show the number of attempts
    label_attempts = tk.Label(window, text="", font=("Arial", 12))
    label_attempts.pack(pady=5)

    # Start the Tkinter event loop
    window.mainloop()

# Run the game when the script is executed
if __name__ == "__main__":
    number_guessing_game()
